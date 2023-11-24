from IPython.display import display, HTML

data = {
    "name": "A corp",
    "children": [
        {
            "name": "A corp",
            "children": [
                {"name": "A corp"},
                {"name": "A corp international"},
                {"name": "A corp domestic"}
            ]
        },
        {
            "name": "A international",
            "children": [
                {"name": "A corp bus"},
                {"name": "A corp car"}
            ]
        },
        {
            "name": "A domestic",
            "children": [
                {"name": "A corp carpool"},
                {"name": "A corp wagon"}
            ]
        }
    ]
}

html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Tidy Tree using D3.js</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
    <svg width="600" height="400"></svg>

    <script>
        var data = {data};

        var width = 600;
        var height = 400;

        var svg = d3.select("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", "translate(50, 50)");

        var treeLayout = d3.tree().size([width - 100, height - 100]);
        var root = d3.hierarchy(data);
        treeLayout(root);

        var links = root.links();
        var linkPathGenerator = d3.linkHorizontal()
            .x(d => d.y)
            .y(d => d.x);

        svg.selectAll("path.link")
            .data(links)
            .enter()
            .append("path")
            .attr("class", "link")
            .attr("d", linkPathGenerator);

        var nodes = root.descendants();
        svg.selectAll("circle.node")
            .data(nodes)
            .enter()
            .append("circle")
            .attr("class", "node")
            .attr("cx", d => d.y)
            .attr("cy", d => d.x)
            .attr("r", 4);

        svg.selectAll("text.label")
            .data(nodes)
            .enter()
            .append("text")
            .attr("class", "label")
            .attr("x", d => d.y)
            .attr("y", d => d.x)
            .attr("dy", "0.35em")
            .text(d => d.data.name);
    </script>
</body>
</html>
"""

display(HTML(html_template))
