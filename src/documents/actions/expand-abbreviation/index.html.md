---
layout: page
title: 展开缩写
menuOrder: 1
---
Expands [CSS-like abbreviations](/abbreviations/) into HTML/XML/CSS code, depending on current document’s syntax. Also performs other context actions, for example, transforms [CSS Gradient](/css-abbreviations/gradients/).

依据当前文档的语法，将类似于 CSS 的[缩写](/abbreviations/)展开为 HTML/XML/CSS 代码。也能做其它的操作，例如转换 [CSS 渐变](/css-abbreviations/gradients/)。

<textarea class="movie-def">
&lt;html&gt;
&lt;head&gt;
	&lt;title&gt;Demo&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
	|
&lt;/body&gt;
&lt;/html&gt;
~~~
tooltip: Type a CSS-like abbreviation
type: #page>(#header>ul#nav>li*4>a)+(#content>h1{Hello world}+p)+#footer
wait: 1000
tooltip: Run “Expand Abbreviation” action ::: “Expand Abbreviation” (Tab key)
run: emmet.expand_abbreviation
</textarea>

Generated output contains a number of _tabstops_ and if your editor supports them (Eclipse, Sublime Text 2, Espresso etc) you can quickly traverse between them with Tab key.

如果你的编辑器(Eclipse, Sublime Text 2, Espresso 等)支持插入占位，生成的代码包括多个插入占位，这样可以用 Tab 键在它们之间快速移动。

In some editors (Eclipse, Sublime Text 2, CodeMirror) “Expand Abbreviation” can be invoked with Tab key.

一些编辑器(Eclipse, Sublime Text 2, CodeMirror)，可以用 Tab 键触发 “展开缩写”功能。