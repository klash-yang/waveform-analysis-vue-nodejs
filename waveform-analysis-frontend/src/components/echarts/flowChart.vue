<template>
  <div class="right-upper-wrap">
    <v-chart :options="chartOptionsBar"/>
  </div>
</template>

<script>
// import echarts from 'echarts'
import ECharts from 'vue-echarts'
//import 'echarts/lib/chart/line'
//import 'echarts/lib/component/polar'
import { dataRequest } from '../../request/dataRequest';

export default {
  components: {
    'v-chart': ECharts
  },
  data: () => ({
    chartOptionsBar: {},
    wav: []
  }),
  methods: {
    fillChart: function() {
      this.items = [];
      let chartOptionsBar = {
        xAxis: {
            data: []
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
            type: 'line',
            data: []
            }
        ]
      }
      for(let i = 0; i < this.wav.length; i++) {
        chartOptionsBar.xAxis.data.push(i + 1);
        chartOptionsBar.series[0].data.push(this.wav[i]);
      }
      this.chartOptionsBar = chartOptionsBar;
    }
  },
  mounted: async function() {
    const resp = await dataRequest();
    if (resp.data) {
      console.log(resp);
      this.wav = resp.data.wav;
    }
    this.fillChart();
  }
}
</script>

<style scoped>
.right-upper-wrap {
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 5px;
}
.echarts {
  width: 100%;
  height: 100%;
}
</style>