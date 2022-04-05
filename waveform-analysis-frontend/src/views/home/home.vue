<template>
  <div>
    <Row>
      <Col span="6" style="padding-right: 5px">
        <info-card
          iconType="ios-arrow-forward"
          color="#2d8cf0"
          :count="onset.toString()"
          message="Inhale">
        </info-card>
      </Col>
      <Col span="6" style="padding-right: 5px">
      <info-card
        iconType="ios-cloud-upload"
        color="#64d572"
        count="Nan"
        message="Inhale Pause"></info-card>
      </Col>
      <Col span="6" style="padding-right: 5px">
      <info-card
        iconType="ios-arrow-forward"
        color="#ffd572"
        :count="offset.toString()"
        message="Exhale"></info-card>
      </Col>
      <Col span="6" >
      <info-card
        iconType="ios-cloud-upload"
        color="#f25e43"
        count="Nan"
        message="Exhale Pause"></info-card>
      </Col>
    </Row>

    <Row style="padding-top: 10px">
      <Col span="12">
      <Card>
        <p slot="title" class="card-title">
          <Icon type="ios-shuffle-strong"></Icon>
          Breath table 
        </p>
        <div class="breath-table">
          <Table stripe :columns="tableTitle" :data="tableData" no-data-text="No Data" height="200"></Table>
        </div>
      </Card>
      </Col>
      
      <Col span="12">
      <Card>
        <p slot="title" class="card-title">
          <Icon type="ios-shuffle-strong"></Icon>
          Flow Waveform 
        </p>
        <div class="line-chart-con">
          <line-chart :wav="wav"></line-chart>
        </div>
      </Card>
      </Col>
    </Row>
    
    <Row style="padding-top: 10px">
      <Col span="8" style="padding-right: 5px">
      <Card>
        <p slot="title" class="card-title">
          <Icon type="android-wifi"></Icon>
          Flow Gauge

        </p>
        <div style="height: 200px">
          <gauge-chart></gauge-chart>
        </div>
      </Card>
      </Col>
      <Col span="8" style="padding-right: 5px">
      <Card>
        <p slot="title" class="card-title">
          <Icon type="android-wifi"></Icon>
          Statistics1

        </p>
        <div style="height: 200px">
          <pie-chart></pie-chart>
        </div>
      </Card>
      </Col>
      <Col span="8" >
      <Card>
        <p slot="title" class="card-title">
          <Icon type="android-wifi"></Icon>
          Statistics2

        </p>
        <div style="height: 200px">
          <shadow-chart></shadow-chart>
        </div>
      </Card>
      </Col>

    </Row>

  </div>
</template>

<script>
  import infoCard from '../../components/info-card/infoCard.vue'
  import lineChart from '../../components/echarts/lineChart.vue'
  import gaugeChart from '../../components/echarts/gaugeChart.vue'
  import pieChart from '../../components/echarts/pieChart.vue'
  import shadowChart from '../../components/echarts/shadowChart.vue'
  // added xuyong
  import flowChart from '../../components/echarts/flowChart.vue'
  import { dataRequest } from '../../request/dataRequest';
  import client from '../../request/websocket';
  

  export default {
    components: {
      infoCard,
      lineChart,
      gaugeChart,
      pieChart,
      shadowChart,
      //added xuyong
      flowChart
    },
    data: () => {
      return {
        tableTitle: [
          {title: 'Breath', key: 'breath'},
          {title: 'Onset', key: 'onset'},
          {title: 'Offset', key: 'offset'}
        ],
        tableData: [],
        onset: 0,
        offset: 0,
        index: 0,
        onsetArr: [],
        offsetArr: [],
        wav: []
      }
    },
    methods: {
      fillTable: function(data) {
        this.items = [];
        for(let i = 0; i < data.col1.length; i++) {
          this.tableData.push({breath: data.col1[i], onset: data.col2[i], offset: data.col3[i]});
        }
      },
      AIClick: function() {
        window.open('http://localhost:8081', '_blank');
      },
      updateData: function() {
        setInterval(() => {
          if (this.index < this.onsetArr.length) {
            this.onset = this.onsetArr[this.index];
            this.offset = this.offsetArr[this.index];
            this.index++
          }
        }, 1000);
      },
      receiveData: function(data) {
        this.onsetArr = [...this.onsetArr, ...data.inh];
        this.offsetArr = [...this.offsetArr, ...data.exh];
        this.wav = [...this.wav, ...data.wav];
      }
    },
    mounted: async function() {
      try {
        client.onmessage = (e) => {
          let data = JSON.parse(e.data);
          console.log(data);
          this.receiveData(data);
        }
      } catch(e) {
        console.log(e);
      }
      this.updateData();
      const resp = await dataRequest();
      console.log(resp)
      if (resp.data) {
        this.fillTable(resp.data);
      }
    }
  }
</script>

<style>
  .line-chart-con{
    height: 200px;
  }
</style>
