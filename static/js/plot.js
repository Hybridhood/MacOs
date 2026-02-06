const xArray = stockData.x;
const yArray = stockData.y;
alert(xArray);
// Define Data
const data = [{
  x: xArray,
  y: yArray,
  mode: "lines",
  type: "scatter"
}];

// Define Layout
const layout = {
  xaxis: {range: [1, 400], title: "Square Meters"},
  yaxis: {range: [1, 400], title: "Price in Millions"},
  title: "House Prices vs Size"
};

// Display using Plotly
Plotly.newPlot("myPlot", data, layout);