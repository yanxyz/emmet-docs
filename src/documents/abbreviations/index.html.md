---
layout: page
title: 缩写
menuOrder: 1
---
Abbreviations are the heart of the Emmet toolkit: these special expressions are parsed in runtime and transformed into structured code block, HTML for example. The abbreviation’s syntax looks like CSS selectors with a few extensions specific to code generation. So every web-developer already knows how to use it.

缩写是 Emmet 的核心：这些特殊的表达式被实时的解析转化为代码块。缩写的语法类似于 CSS 选择器，每个网页开发者都知道怎么用。

Here’s an example: this abbreviation

例如这个缩写：

	#page>div.logo+ul#navigation>li*5>a{Item $}

...can be transformed into

	<div id="page">
		<div class="logo"></div>
		<ul id="navigation">
			<li><a href="">Item 1</a></li>
			<li><a href="">Item 2</a></li>
			<li><a href="">Item 3</a></li>
			<li><a href="">Item 4</a></li>
			<li><a href="">Item 5</a></li>
		</ul>
	</div>

...with	just a single key stroke. In many editors (such as Eclipse, Sublime Text 2, Espresso etc.) plugins will also generate proper _tabstop marks_ so you can quickly traverse between important places of generated code with the Tab key.

许多编辑器（比如 Eclipse, Sublime Text 2, Espresso 等） 的插件也生成插入占位，使用 Tab 键可以快捷在这些重要的地方跳转。

Abbreviations are optimised for, but not limited to, HTML and XML generation, and make writing tedious markup code a breeze. You can start learning [syntax](/abbreviations/syntax/) to unleash the full power of Emmet abbreviations.

缩写最适合于生成 HTML/XML，但是不限于此。下面开始学习[语法](/abbreviations/syntax/)来了解 Emmet 缩写的强大。