/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // const dt = [
  //   15,
  //   21,
  //   18,
  //   243,
  //   239,
  //   92,
  //   14,
  // ]

  // Graphs
  const ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  const myChart = new Chart(ctx, {
    type: 'bar', //line
    data: {
      labels: [ dy2
        
        // 'Sunday',
        // 'Monday',
        // 'Tuesday',
        // 'Wednesday',
        // 'Thursday',
        // 'Friday',
        // 'Saturday'
      ],
      datasets: [{
        data: dt2,
        lineTension: 0,
        backgroundColor: '#007bff', //'transparent', 
        borderColor: '#007bff',
        borderWidth: 0, //4
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          boxPadding: 3
        }
      }
    }
  })
})()
