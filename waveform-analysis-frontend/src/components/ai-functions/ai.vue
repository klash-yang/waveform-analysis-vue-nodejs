
<template>
  <div>
  <Row style="padding-top: 10px">
      <Col span="10" style="padding-right: 5px">
      
      <Card>
        <p slot="title" class="card-title">
          <Icon type="android-wifi"></Icon>
          Respiratory Pattern Recognition
        </p>
        <div style="height: 200px">
          <div id="shadowChart" style="width:100%;height: 100%"></div>
        </div>

        <div class="btn-1">
        <Button type="primary">Dignosis: Regular</Button>
        </div>

      </Card>
      </Col>
    </Row>
  </div>
</template>


<script>
  import echarts from 'echarts'
  import { dataRequest } from '../../request/dataRequest';

  export default {
    name: 'lineChart',
    props: {
      chartOptions: Object,
      chartData: Object

    },
    methods: {
      init (types) {
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
            data: ['Eupnea', 'Tachypnea', 'Biots', 'Bradypnea', 'Cheyne-Stokes'],
            nameTextStyle: {
              color: '#c3c3c3'
            }
          },
          series: [
            {
              name: 'amount',
              type: 'bar',
              data: []
            }
          ]
        };
        option.series[0].data.push(types.type1)
        option.series[0].data.push(types.type2)
        option.series[0].data.push(types.type3)
        option.series[0].data.push(types.type4)
        option.series[0].data.push(types.type5)
        const shadowChart = echarts.init(document.getElementById('shadowChart'))
        shadowChart.setOption(option)

        window.addEventListener('resize', function () {
          shadowChart.resize()
        })
      }

    },

     mounted: async function() {
      const resp = await dataRequest();
      console.log(resp)
      if (resp.data) {
        this.init(resp.data);
      }
    }
  }
</script>
