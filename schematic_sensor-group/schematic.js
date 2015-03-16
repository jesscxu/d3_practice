var width = 960,
    height = 500;

var nodes = [
    { x: width/5, y: height/5 },
    { x: width/5, y: 2*height/5 },
    { x: width/5, y: 3*height/5 },
    { x: 2*width/5, y: 2*height/5 },
    { x: 3*width/5, y: 2*height/5 },
    { x: 3.5*width/5, y: 4*height/5 },
    { x: 4*width/5, y: 1.5*height/5 },
    { x: 4.45*width/5, y: 3.5*height/5 }
];



var links = [
    { source: 0, target: 3 },
    { source: 1, target: 3 },
    { source: 2, target: 3 },
    { source: 3, target: 4 },
    { source: 4, target: 5 },
    { source: 4, target: 6 },
    { source: 5, target: 6 },
    { source: 6, target: 5 },
    { source: 6, target: 7 }
];



var force = d3.layout.force()
    .nodes(nodes)
    .links(links)
    .size([width, height]);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);


  svg.selectAll("line")
      .data(links)
    .enter().append("line")
      .attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; })



  svg.selectAll("circle")
      .data(nodes)
    .enter().append("circle")
      .attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; })
      .attr("r", 4.5);

      