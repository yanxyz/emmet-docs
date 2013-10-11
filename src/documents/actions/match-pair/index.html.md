---
layout: page
title: 匹配标签
menuOrder: 2
---
A well-known tag balancing: searches for tag or tag's content bounds from current caret position and selects it. It will expand (outward balancing) or shrink (inward balancing) selection when called multiple times. Not every editor supports both inward and outward balancing due of some implementation issues, most editors have outward balancing only.

从插入符所在位置开始查找标签及标签内容，并选中它。当多次调用时将向外扩展或向内收缩选择。由于实现上的问题，不是所有的编辑器同时支持这两种操作，多数编辑器只支持向外扩展选择。

<textarea class="movie-def">
&lt;div id="page"&gt;
	&lt;section class="content"&gt;
		&lt;h1&gt;Document example&lt;/h1&gt;
		&lt;p&gt;Lorem ipsum |dolor sit amet.&lt;/p&gt;
	&lt;/section&gt;
&lt;/div&gt;
@@@
tooltip: Place caret inside tag’s content and run “Match Pair” action to select it
run: emmet.match_pair_outward ::: “Match Pair Outward” (Cmd-D)
wait: 1000
tooltip: Run action multiple times to expand selection
run: {command: 'emmet.match_pair_outward', times: 5}
wait: 1000
tooltip: Run “Match Pair Inward” action to shrink selection
wait: 1000
run: {command: 'emmet.match_pair_inward', times: 5} ::: “Match Pair Inward (Shift-Cmd-D)
</textarea>

Emmet’s tag balancing is quite unique. Unlike other implementation, this one will search tag bounds from caret’s position, not the start of the document. It means you can use tag balancer even in non-HTML documents.

Emmet 的匹配标签功能很独特。不像其它实现，Emmet 从插入符所在位置而不是从文档的开头开始搜索标签，这意味着可以在非 HTML 文档使用这个功能。

<textarea class="movie-def">
function test(data) {
	var out = '&lt;table&gt;';
	for (var i = data.rows.length - 1; i >= 0; i--) {
		var row = data.rows[i];
		out += '&lt;tr&gt;';

		for (var j = row.cells.length - 1; j >= 0; j--) {
			out += '&lt;td&gt;' + row.|cells[j] + '&lt;/td&gt;';
		}

		out += '&lt;/tr&gt;';
	}

	out += '&lt;/table&gt;';
	return out;
}
@@@
tooltip: {text: 'Place caret somewhere between opening and closing tag. Run “Match Pair” action and, if tag definitions are consistent enough, they will match', wait: 7000}
run: {command: 'emmet.match_pair_outward', times: 6} ::: “Match Pair” (Cmd-D)
@@@
mode: text/javascript
</textarea>

Note that tag matching may not work outside HTML if tag definition is assembled by concatenating strings, like this: `var cell = '<td class="' + (data.odd ? 'odd' : 'even') + '">'`;

注意如果标签是由拼接的字符定义，像这样：`var cell = '<td class="' + (data.odd ? 'odd' : 'even') + '">'`，不能匹配标签。