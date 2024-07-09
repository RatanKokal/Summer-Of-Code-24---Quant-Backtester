var labels = data.labels;
var stock_cummulative_returns = data.stock_cummulative_return;
var nifty_cummulative_returns = data.nifty_cummulative_return;
var myChart;  // Declare myChart variable outside the DOMContentLoaded event listener

document.addEventListener('DOMContentLoaded', function() {
    // Function to initialize or re-render the chart
    function initChart() {
        // Clear existing chart instance if it exists
        if (myChart) {
            myChart.destroy();
        }

        var ctx = document.getElementById('myChart').getContext('2d');
        myChart = new Chart(ctx, {
            type: 'line',  // Specify the chart type
            data: {
                labels: labels,  // X-axis labels (datetime)
                datasets: [{
                    label: ticker,  // Dataset label
                    data: stock_cummulative_returns,  // Data points for the chart (cumulative returns)
                    borderColor: 'blue',  // Line color
                    backgroundColor: 'transparent'  // No fill color
                },
                {
                    label: 'NIFTY50',  // Dataset label
                    data: nifty_cummulative_returns,  // Data points for the chart (cumulative returns)
                    borderColor: 'red',  // Line color
                    backgroundColor: 'transparent'  // No fill color
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    zoom: {
                        zoom: {
                            wheel: {
                                enabled: true,
                            },
                            pinch: {
                                enabled: true
                            },
                        },
                        pan: {
                            enabled: true,
                        },
                    }
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Date(time)'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Cummulative Returns'
                        }
                    }
                }
            }
        });
    }

    // Initialize the chart on page load
    initChart();

    // Event listener for orientation change
    window.addEventListener('orientationchange', function() {
        myChart.resize();
        myChart.resetZoom();
    });

    // Reset zoom button functionality
    document.getElementById('resetZoomBtn').addEventListener('click', function() {
        myChart.resetZoom();
    });

    function openFullscreen(elem) {
        if (document.fullscreenElement || document.webkitFullscreenElement || document.msFullscreenElement) {
            document.exitFullscreen();
        } else if (elem.requestFullscreen) {
          elem.requestFullscreen();
        } else if (elem.webkitRequestFullscreen) { /* Safari */
          elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) { /* IE11 */
          elem.msRequestFullscreen();
        }
    }

    document.getElementById('fullScreenBtn').addEventListener('click', function() {
        openFullscreen(document.getElementsByClassName('container')[1]);
    });

});
