var stock_chart_one = document.getElementById("stock_chart_one");
if (stock_chart_one !== null){
    var echart_one = echarts.init(stock_chart_one);

    var option_one = {
        title:{
            text: JSON.parse(document.getElementById("ticker_one_name").textContent)
        },
        tooltip:{
            trigger: 'axis'
        },
        legend: {
            top: 5,
            data: ["Opening Prices", "Closing Prices", "Adjusted Closing Prices"],
            selected: {"Opening Prices": true, "Closing Prices": true, "Adjusted Closing Prices": false},
            itemGap: 50
        },
        xAxis: {
            type: "category",
            data: JSON.parse(document.getElementById("ticker_one_dates").textContent)
        },
        yAxis: {},
        toolbox: {
            right: 10,
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            }
        },
        dataZoom: [
            {
                startValue: '2014-06-01'
            },
            {
                type: 'inside'
            }
        ],
        series: [
            {
                name: "Opening Prices",
                data: JSON.parse(document.getElementById("ticker_one_opens").textContent),
                type: "line",
                colorBy: "series",
                symbol: "rect",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "-50%"],
                }
            },
            {
                name: "Closing Prices",
                data: JSON.parse(document.getElementById("ticker_one_closes").textContent),
                type: "line",
                colorBy: "series",
                symbol: "diamond",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "50%"],
                }
            },
            {
                name: "Adjusted Closing Prices",
                data: JSON.parse(document.getElementById("ticker_one_adj_closes").textContent),
                type: "line",
                colorBy: "series",
                symbol: "circle",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "50%"],
                }
            },
        ]
    };

    echart_one.setOption(option_one);
};

// ==================================================================================================================

var stock_chart_two = document.getElementById("stock_chart_two");
if (stock_chart_two !== null){
    var echart_two = echarts.init(stock_chart_two);
    var option_two = {
        title:{
            text: JSON.parse(document.getElementById("ticker_two_name").textContent)
        },
        tooltip:{
            trigger: 'axis'
        },
        legend: {
            top: 5,
            data: ["Opening Prices", "Closing Prices", "Adjusted Closing Prices"],
            selected: {"Opening Prices": true, "Closing Prices": true, "Adjusted Closing Prices": false},
            itemGap: 50
        },
        xAxis: {
            type: "category",
            data: JSON.parse(document.getElementById("ticker_two_dates").textContent)
        },
        yAxis: {},
        toolbox: {
            right: 10,
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            }
        },
        dataZoom: [
            {
                startValue: '2014-06-01'
            },
            {
                type: 'inside'
            }
        ],
        series: [
            {
                name: "Opening Prices",
                data: JSON.parse(document.getElementById("ticker_two_opens").textContent),
                type: "line",
                colorBy: "series",
                symbol: "rect",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "-50%"],
                }
            },
            {
                name: "Closing Prices",
                data: JSON.parse(document.getElementById("ticker_two_closes").textContent),
                type: "line",
                colorBy: "series",
                symbol: "diamond",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "50%"],
                }
            },
            {
                name: "Adjusted Closing Prices",
                data: JSON.parse(document.getElementById("ticker_two_adj_closes").textContent),
                type: "line",
                colorBy: "series",
                symbol: "circle",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "50%"],
                }
            },
        ]
    };

    echart_two.setOption(option_two);
};



// ==================================================================================================================

var stock_chart_three = document.getElementById("stock_chart_three");
if (stock_chart_three !== null){
    var echart_three = echarts.init(stock_chart_three);

    var option_three = {
        title:{
            text: JSON.parse(document.getElementById("ticker_three_name").textContent)
        },
        tooltip:{
            trigger: 'axis'
        },
        legend: {
            top: 5,
            data: ["Opening Prices", "Closing Prices", "Adjusted Closing Prices"],
            selected: {"Opening Prices": true, "Closing Prices": true, "Adjusted Closing Prices": false},
            itemGap: 50
        },
        xAxis: {
            type: "category",
            data: JSON.parse(document.getElementById("ticker_three_dates").textContent)
        },
        yAxis: {},
        toolbox: {
            right: 10,
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            }
        },
        dataZoom: [
            {
                startValue: '2014-06-01'
            },
            {
                type: 'inside'
            }
        ],
        series: [
            {
                name: "Opening Prices",
                data: JSON.parse(document.getElementById("ticker_three_opens").textContent),
                type: "line",
                colorBy: "series",
                symbol: "rect",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "-50%"],
                }
            },
            {
                name: "Closing Prices",
                data: JSON.parse(document.getElementById("ticker_three_closes").textContent),
                type: "line",
                colorBy: "series",
                symbol: "diamond",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "50%"],
                }
            },
            {
                name: "Adjusted Closing Prices",
                data: JSON.parse(document.getElementById("ticker_three_adj_closes").textContent),
                type: "line",
                colorBy: "series",
                symbol: "circle",
                //            label: {
                //                show: true,
                //                position:"bottom"
                //            },
                markPoint: {
                    data: [
                        {
                            type: "max"
                        },
                        {
                            type: "min"
                        },
                        {
                            type: "average"
                        }
                    ],
                    symbol: "diamond",
                    symbolSize: 25,
                    symbolOffset: ["0%", "50%"],
                }
            },
        ]
    };

    echart_three.setOption(option_three);
}