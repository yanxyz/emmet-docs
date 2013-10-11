---
layout: page
title: 跳转到配对标签
menuOrder: 2.5
---
In HTML, allows you to quickly traverse between opening and closing tag:

在HTML标签的开始与关闭标记间跳转。

<textarea class="movie-def">
&lt;div id="page"&gt;
	&lt;section class="content"&gt;
		&lt;h1&gt;Document example&lt;/h1&gt;
		&lt;p&gt;Lorem ipsum dolor sit amet.&lt;/p&gt;
	&lt;/section&gt;
&lt;/|div&gt;
~~~
tooltip: {text: 'Place caret inside either opening or closing tag and run “Go to Matching Pair” action to go to the opposite tag pair', wait: 7000}
wait: 1000
run: {command: 'emmet.matching_pair', times: 5} ::: “Go to Matching Pair” (Cmd-T)
</textarea>

----------------

“Go to Matching Pair” action uses “[HTML Matcher](/actions/match-pair/)” internally so it may work in non-HTML syntaxes too.

这个功能在内部调用 [匹配标签](/actions/match-pair/) 功能，所以非 HTML 语法也可以用。
