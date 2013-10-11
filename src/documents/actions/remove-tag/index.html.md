---
layout: page
title: 删除标签
menuOrder: 8
---
Quickly removes tag, found by “[Match Tag Pair](/actions/match-pair/)” from current caret position, and adjusts indentation.

快速删除标签，并调整缩进。这里的标签是在插入符所在位置由 [匹配标签](/actions/match-pair/) 功能查找的标签。

<textarea class="movie-def">
&lt;body&gt;
	&lt;div |class="wrapper"&gt;
		&lt;h1&gt;Title&lt;/h1&gt;
		&lt;p&gt;Lorem ipsum dolor sit amet.&lt;/p&gt;
		&lt;p&gt;Officiis animi consequuntur iure.&lt;/p&gt;
		&lt;p&gt;Ea asperiores aperiam non necessitatibus?&lt;/p&gt;
		&lt;p&gt;Expedita iusto cupiditate eum esse.&lt;/p&gt;
	&lt;/div&gt;
&lt;/body&gt;
~~~
tooltip: Place caret somewhere “Match Tag Pair” action can find tag definition
wait: 1000
run: emmet.remove_tag ::: “Remove Tag” (Cmd-K)
</textarea>

----------------

“Remove Tag” action uses “[HTML Matcher](/actions/match-pair/)” internally so it may work in non-HTML syntaxes too.

这个功能在内部调用 [匹配标签](/actions/match-pair/) 功能，所以非 HTML 语法也可以用。