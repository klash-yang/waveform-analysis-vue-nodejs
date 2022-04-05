<template>
  <div id="shadowChart" style="width:100%;height: 100%"></div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    name: 'lineChart',
    props: {
      chartOptions: Object,
      chartData: Object

    },
    methods: {
      init () {
        let  option = {
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          grid: {
            top: 0,
            left: '2%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
          },
          yAxis: {
            type: 'category',
            data: ['Minute ventilation', 'Inhaled Tidal Volume', 'Exhaled Tidal Volume', 'Tidal Volume'],
            nameTextStyle: {
              color: '#c3c3c3'
            }
          },
          series: [
            {
              name: 'volume',
              type: 'bar',
              data: [
                {value: 5250, name: 'Minute ventilation', itemStyle: {normal: {color: '#2d8cf0'}}},
                {value: 439, name: 'Inhaled Tidal Volume', itemStyle: {normal: {color: '#2d8cf0'}}},
                {value: 543, name: 'Exhaled Tidal Volume', itemStyle: {normal: {color: '#2d8cf0'}}},
                {value: 1050, name: 'Tidal Volume', itemStyle: {normal: {color: '#2d8cf0'}}}
              ]
            }
          ]
        };
        const shadowChart = echarts.init(document.getElementById('shadowChart'))
        shadowChart.setOption(option)

        window.addEventListener('resize', function () {
          shadowChart.resize()
        })
      }

    },
    mounted () {
      this.init()
    }
  }
</script>
