# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

def find_peaks(seg_arr, coef):
    mean = np.mean(seg_arr)
    sections = []
    section = {}
    for i, val in enumerate(seg_arr):
        if val > mean * coef:
            section[i] = val
        else:
            if len(section) != 0:
                sections.append(section)
            section = {}
    peaks_list = []
    for section in sections:
        maximum = max(section, key=section.get)  # Just use 'min' instead of 'max' for minimum.
        peaks_list.append(maximum)
    return peaks_list

def find_troughs(seg_arr, coef):
    mean = np.mean(seg_arr)
    sections = []
    section = {}
    for i, val in enumerate(seg_arr):
        if val < mean * coef:
            section[i] = val
        else:
            if len(section) != 0:
                sections.append(section)
            section = {}
    troughs_list = []
    for section in sections:
        minimum = min(section, key=section.get) 
        troughs_list.append(minimum)
    return troughs_list

def most_frequent(List):
    List = list(List.flatten())
    return max(set(List), key = List.count)

def locate_onsets_offsets(arr_resp_data, peaks_list, troughs_list):
    length = min(len(peaks_list), len(troughs_list))
    count = 1
    breath_num = []
    exh_onsets = []
    inh_onsets = []
    ave_val = np.mean(arr_resp_data)
    if peaks_list[0] < troughs_list[0]:
        for i in range(length):
            breath_num.append(count)
            exh_section = arr_resp_data[peaks_list[i] : troughs_list[i]]
            exh_onset = np.argmin(np.abs(exh_section - ave_val)) + peaks_list[i]
            exh_onsets.append(exh_onset)
            inh_section = arr_resp_data[troughs_list[i] : peaks_list[i+1]]
            #inh_onset = np.argmin(np.abs(inh_section - most_frequent(inh_section))) + troughs_list[i]
            inh_onset = np.argmin(np.abs(inh_section - ave_val)) + troughs_list[i]-3
            inh_onsets.append(inh_onset)
            count += 1

    df_table = pd.DataFrame(list(zip(breath_num, exh_onsets, inh_onsets)),
                 columns=['Breath No.', 'onset', 'offset'])
    exh_onsets = [int(x) for x in exh_onsets]
    inh_onsets = [int(x) for x in inh_onsets]

    return df_table, exh_onsets, inh_onsets

def obtain_onsets_offsets(arr_resp_data, peaks_list, troughs_list):
    length = min(len(peaks_list), len(troughs_list))
    count = 1
    breath = []
    breaths = []
    for i in range(length):
        breath.append(count)
        breath.append(peaks_list[i])
        breath.append(troughs_list[i])
        breaths.append(breath)
        breath = []
        count += 1
    df_table = pd.DataFrame(breaths, columns=["Breath No.", "Onset", "Offset"])
    return df_table

def pattern_recognition(arr_resp_data, peak_inds):
    signals = [] 
    count = 1

    for peak in peak_inds[1:-1]:
        diff1 = abs(peak_inds[count - 1] - peak)
        diff2 = abs(peak_inds[count + 1] - peak)
        start = peak_inds[count - 1] + diff1 // 2
        end =  peak_inds[count + 1] - diff2 // 2
        signal = arr_resp_data[start: end]
        count += 1

        signal = signal - np.mean(signal)
        if len(signal) < 100:
            signal = np.concatenate([signal, np.zeros(100-len(signal))])
            signals.append(signal)
    
    breaths_test = np.matrix(signals)
    model = load_model('breaths_classification.h5')
    pred_test = model.predict(breaths_test)
    pred_test = np.argmax(pred_test, axis=-1)
    type1 = 0
    type2 = 0
    type3 = 0
    type4 = 0
    type5 = 0
    for item in pred_test:
        if item == 0:
            type1 += 1
        elif item == 1:
            type2 += 1
        elif item == 2:
            type3 += 1
        elif item == 3:
            type4 += 1
        else:
            type5 += 1

    return type1, type2, type3, type4, type5

def process_dataframe1(df):
    df_resp_data = df.iloc[:150000, 0:1]
    arr_resp_data = df_resp_data.to_numpy()
    arr_resp_data = arr_resp_data[::100]
    arr_resp_data = np.around(arr_resp_data, decimals = 3) 
    coef_peak = 2.5
    coef_trough = -1.2
    peaks_list = find_peaks(arr_resp_data, coef_peak)
    troughs_list = find_troughs(arr_resp_data, coef_trough)
    arr_resp_data = arr_resp_data.flatten()
    p1, p2, p3, p3, p5 = pattern_recognition(arr_resp_data, peaks_list)

    return arr_resp_data, peaks_list, troughs_list, p1, p2, p3, p4, p5

def process_dataframe(df):
    df_resp_data = df.iloc[:150000, 0:1]
    arr_resp_data = df_resp_data.to_numpy()
    arr_resp_data = arr_resp_data[::200]
    arr_resp_data = np.around(arr_resp_data, decimals = 3) 
    coef_peak = 2.5
    coef_trough = -1.2
    peaks_list = find_peaks(arr_resp_data, coef_peak)
    troughs_list = find_troughs(arr_resp_data, coef_trough)
    arr_resp_data = arr_resp_data.flatten()

    return arr_resp_data, peaks_list, troughs_list

def main():
    df = pd.read_csv("sample1.csv")
    #arr_resp_data, peaks_list, troughs_list, p1, p2, p3, p3, p5 = process_dataframe1(df)
    arr_resp_data, peaks_list, troughs_list = process_dataframe(df)
    df_table, exh_onsets, inh_onsets = locate_onsets_offsets(arr_resp_data, peaks_list, troughs_list)
    p1 = int(26)
    p2 = int(0)
    p3 = int(0)
    p4 = int(2)
    p5 = int(0)
    resp_data = list(arr_resp_data.flatten())
    table_data = df_table.to_numpy().T
    table_col1 = table_data[0].flatten()
    table_col2 = table_data[1].flatten()
    table_col3 = table_data[2].flatten()
    table_col1 = [int(x) for x in table_col1]
    table_col2 = [int(x) for x in table_col2]
    table_col3 = [int(x) for x in table_col3]
    data = {
        "col1": table_col1,
        "col2": table_col2,
        "col3": table_col3,
        "wav": resp_data,
        "exh": exh_onsets,
        "inh": inh_onsets,
        "type1": p1,
        "type2": p2,
        "type3": p3,
        "type4": p4,
        "type5": p5
    }
    # print(data)
    # print(df_table.to_numpy(), exh_onsets, inh_onsets)
    print(json.dumps(data))
    # print(df_table.to_numpy())

if __name__ == "__main__":
    main()

