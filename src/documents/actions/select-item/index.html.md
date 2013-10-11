---
layout: page
title: 选择
menuOrder: 5
---
Action is similar to [“Go to Edit Point”](/actions/go-to-edit-point/), but selects important code parts.

这个功能类似于[编辑点间移动](/actions/go-to-edit-point/)功能，但是选择重要的代码部分。

In HTML, these are tag name, full attribute and attribute value. For class attribute it also selects distinct classes.

对于 HTML，选择标签名，完整的属性与属性值。对于 class 属性也选择不同的 class。

<textarea class="movie-def">
|&lt;section&gt;
	&lt;p&gt;&lt;/p&gt;
	&lt;div class="main footer"&gt;&lt;/div&gt;

    &lt;script&gt;var str = '<div class="main footer"></div>';&lt;/script&gt;
&lt;/section&gt;
@@@
run: {command: 'emmet.select_next_item', times: 7} ::: “Select Next Item” (Shift-Cmd-.)
wait: 1000
run: {command: 'emmet.select_previous_item', times: 6} ::: “Select Previous Item” (Shift-Cmd-,)
wait: 1000
moveTo: 4:12
wait: 1000
tooltip: “Select Item” action may also work in non-HTML syntaxes
wait: 500
run: {command: 'emmet.select_next_item', times: 5}
</textarea>

In CSS, it matches selector, full property and property value. For complex values and functions like `1px solid red` or `url(image.jpg)` also selects part of it.

对于 CSS，选择选择器，完整的属性与属性值。对于复杂的值比如 `1px solid red` 或 `url(image.jpg)` 也选择子部分。

<textarea class="movie-def">
|body {
	border: 1px solid black;
	background: url(image.jpg) #ccc no-repeat;
}
@@@
run: {command: 'emmet.select_next_item', times: 12} ::: “Select Next Item” (Shift-Cmd-.)
wait: 1000
run: {command: 'emmet.select_previous_item', times: 11} ::: “Select Previous Item” (Shift-Cmd-,)
@@@
mode: text/css
</textarea>