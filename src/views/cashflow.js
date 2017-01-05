import {cloneDeep} from 'lodash';
import * as d3 from 'd3';

let moment = require('moment');

function CashFlowView(data) {
	let datum = cloneDeep(data);
	let dimensions = {height: 1024, width: 1024 * 1.5, margin: {left:100, top: 0, bottom: 100, right: 0}}

	let svg;
	let xScale	= d3.scaleTime().range([0, dimensions.width])
	let yScale	= d3.scaleLinear().range([0, dimensions.height])
	let xAxis	= d3.axisBottom(xScale)

	this.init = function() {
		initData()
		initView()
		makeView()
	}

	function initData() {
		xScale.domain([new Date("01/01/2015"), moment()])
	}

	function initView() {
		svg = d3.select("#cashflowView")
			.append('svg')
			.attr("width", dimensions.width)
			.attr("height", dimensions.height)
			.attr("viewBox", `0 0 ${dimensions.width + dimensions.margin.left} ${dimensions.height + dimensions.margin.bottom}`)
			.attr("preserveAspectRatio", "xMidYMid meet")

		svg.append("g")
			.classed("xAxis", true)
			.attr("transform", "translate(0," + dimensions.height + ")")

			.call(xAxis)
	}

	function makeView() {
		console.log(datum)
		let txt = svg
				.selectAll("g.hai")
				.data([datum])
				.enter()
					.append("g")
					.classed('hai', true);

	}
}

module.exports = CashFlowView