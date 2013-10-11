---
layout: page
title: 跳转到编辑点
menuOrder: 4
---
This action works for HTML code blocks and allows you to quickly traverse between important code points:

这个功能适用于 HTML 代码块，可以在要点之间跳转：

* between tags 标签之间
* empty attributes 空标签
* newlines with indentation 缩进的新行

<textarea class="movie-def">
|&lt;ul&gt;
	&lt;li&gt;&lt;a href=""&gt;&lt;/a&gt;&lt;/li&gt;
	&lt;li&gt;&lt;a href=""&gt;&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;div&gt;
	|
&lt;/div&gt;

&lt;script&gt;
	var str = '&lt;ul&gt;&lt;li&gt;&lt;a&gt;&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;';
&lt;/script&gt;
~~~
run: {command: 'emmet.next_edit_point', times: 9} ::: “Next Edit Point” (Ctrl-Alt-→)
wait: 1000
run: {command: 'emmet.prev_edit_point', times: 9} ::: “Previous Edit Point” (Ctrl-Alt-←)
wait: 1000
moveTo: 9:4
wait: 500
tooltip: You can use “Go to Edit Point” action in non-HTML documents too
run: {command: 'emmet.next_edit_point', times: 4}
</textarea>
