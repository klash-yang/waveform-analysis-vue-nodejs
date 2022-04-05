<template>
  <div id="lineChart" style="width:100%;height:100%"></div>
</template>

<script>
import echarts from 'echarts'
import { dataRequest } from '../../request/dataRequest';
import client from '../../request/websocket';
  
  export default {
    name: 'lineChart',
    props: {
      chartOptions: Object,
      chartData: Object,
      wav: {
        type: Array,
        default: [],
      },
    },
    data: () => {
      return {
        index: 0,
        lineChart: null,
        // wav: [],
        option: {
          title: {
            text: ''
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              label: {
                backgroundColor: '#6a7985'
              }
            }
          },
          legend: {
            data: ['AirFlow']
          },
          toolbox: {
            feature: {
              saveAsImage: {
                title: 'Save as Image'
              }
            }
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: [
            {
              type: 'category',
              boundaryGap: false,
              data: []
            }
          ],
          yAxis: [
            {
              type: 'value'
            }
          ],
          series: [
            {
              name: 'AirFlow',
              type: 'line',
              stack: 'Total',
              areaStyle: {normal: {}},
              data: []
            }
          ],
          animationEasing: 'elasticOut',
          animationDelayUpdate: function (idx) {
              return idx * 5;
          }
        }
      }
    },

    methods: {
      init (wav) {

        this.lineChart = echarts.init(document.getElementById('lineChart'))
        this.lineChart.setOption(this.option)

        window.addEventListener('resize', () => {
          this.lineChart.resize()
        })
      },
      receiveData(data) {
        this.wav = [...this.wav, ...data];
      },
      updateData() {
        setInterval(() => {
          if (this.index < this.wav.length) {
            this.option.xAxis[0].data.push(this.index);
            this.option.series[0].data.push(this.wav[this.index]);
            this.lineChart.setOption(this.option);
            this.index++;
            if (this.index >= 100) {
              this.option.xAxis[0].data.shift();
              this.option.series[0].data.shift();
            }
          }
        }, 100)
      }
    },

    async mounted () {
      let test = [];
      this.init(test);
      console.log('haha')
      // try {
      //   client.onmessage = (e) => {
      //     let data = JSON.parse(e.data).wav;
      //     console.log(data)
      //     this.receiveData(data);
      //   }
      // } catch(e) {
      //   console.log(e);
      // }
      this.updateData();
    }
  }

</script>
