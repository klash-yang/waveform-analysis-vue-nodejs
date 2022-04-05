<template>
  <div id="pieChart" style="width:100%;height: 100%"></div>
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
        let option = {
          title : {
            text: '',
            subtext: '',
            x:'center'
          },
          tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          legend: {
            orient: 'vertical',
            left: 'left',
            data: ['inhale interval','exhale interval','inhale pause','exhale pause']
          },
          series : [
            {
              name: 'time',
              type: 'pie',
              radius : '55%',
              center: ['50%', '60%'],
              data:[
                {value:335, name:'inhale interval'},
                {value:310, name:'exhale interval'},
                {value:89, name:'inhale pause'},
                {value:104, name:'exhale pause'}
              ],
              itemStyle: {
                emphasis: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        };
        const pieChart = echarts.init(document.getElementById('pieChart'))
        pieChart.setOption(option)

        window.addEventListener('resize', function () {
          pieChart.resize()
        })
      }

    },
    mounted () {
      this.init()
    }
  }
</script>
