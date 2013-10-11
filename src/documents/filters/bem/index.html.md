---
layout: page
title: Yandex BEM/OOCSS
menuOrder: 1
---

If you’re writing your HTML and CSS code in [OOCSS](http://coding.smashingmagazine.com/2011/12/12/an-introduction-to-object-oriented-css-oocss/)-style, [Yandex’s BEM](http://coding.smashingmagazine.com/2012/04/16/a-new-front-end-methodology-bem/) style specifically, you will like this filter. It provides some aliases and automatic insertions of common block and element names in classes.

如果你以 [OOCSS](http://coding.smashingmagazine.com/2011/12/12/an-introduction-to-object-oriented-css-oocss/), [Yandex’s BEM](http://coding.smashingmagazine.com/2012/04/16/a-new-front-end-methodology-bem/) 风格书写 HTML 和 CSS 代码，这个过滤器很有用，提供一些别名以及自动向类名插入块和元素名。

In short, BEM introduces three concept types for CSS classes: Block, Element and Modifier. _Block_ is a some sort of a namespace for a semantic sections of HTML page, for example, `search-form`. _Element_ is a part of section, for example, `serch-form__query-string`. _Modifiers_ define variations of block and elements: `search-form_wide` or `search-form_narrow`. Elements in class names are separated with `__` (double underscore) and modifiers are separated with `_` (single underscore).

BEM 简而言之给类名引入了三个概念：块, 元素和修饰符。块近似于 HTML 块的命令空间，例如 `search-form`。元素是块的子部分，例如`serch-form__query-string`，修饰符定义块与元素的变异体：`search-form_wide` 或 `search-form_narrow`。在类名中元素以 `__` (双下划线)分隔，修饰符以 `_` (单下划线)分隔。

While BEM/OOCSS is a great way to maintain and re-use CSS, it may be very tedious to write these class names in plain HTML, even with help of Emmet abbreviations. You have to write the same block or element name in every element of abbreviation:

BEM/OOCSS 是维护和重用 CSS 的好办法，而在 HTML 中书写这些类名很让人烦，即使使用了 Emmet 缩写，你得在每个缩写中书写同样的块或元素名：

	form.search-form.search-form_wide>input.search-form__query-string+input:s.search-form__btn.search-form__btn_large

The `bem` filter allows you to make abbreviation a bit sorter:

`bem` 过滤器可以让缩写简短些：

	form.search-form._wide>input.-query-string+input:s.-btn_large|bem

## How it works 工作原理

BEM filter introduces a few class name prefixes for concept types: `__` or `-` as _element prefix_ and `_` as _modifier prefix_. Whenever you begin the class name with one of these prefixes, filter will resolve the rest parts for you:

BEM 过滤器引入类名前缀：`__` 或 `-` 作为元素前缀， `_` 作为修饰符前缀。当类名前有这些前缀，过滤器将如此解析：

* if you start class name element prefix, filter will resolve _block name_ from _parent_ node;
* 若类名有元素前缀，过滤器从父节点解析块名。
* if you start class name with modifier prefix, filter will resolve _block name_ and/or _element name_ from _current or parent_ nodes;
* 若类名有修饰符前缀，过滤器从当前节点或父节点解析块名或元素名。
* if you use both element and modifier prefixes, filter will resolve _block name_ from parent node and output both “unmodified” and “modified” classes on element;
* 若类名同时有这两种前缀，过滤器从父节点解析块名，并同时向元素添加没有修饰的与修饰过的类名。
* if you use _multiple_ element prefixes, filter with resolve block name from _nth_ parent node.
* 若使用多个元素前缀，过滤器从 _nth_ 父节点解析块名。

Here are a few examples:

示例：

<table>
<tr>
<th>Abbreviation</th>
<th>Output</th>
</tr>
<tr>
<td>`.b_m`</td>
<td>
<pre><code>&lt;div class="b b_m">&lt;/div></code></pre>
</td>
</tr>

<tr>
<td>`.b_m1._m2`</td>
<td>
<pre><code>&lt;div class="b b\_m1 b\_m2">&lt;/div></code></pre>
</td>
</tr>

<tr>
<td>`.b>._m`</td>
<td>
<pre><code>&lt;div class="b">
	&lt;div class="b b\_m">&lt;/div>
&lt;/div></code></pre>
</td>
</tr>

<tr>
<td>`.b1>.b2_m1>.-e1+.--e2_m2`</td>
<td>
<pre><code>&lt;div class="b1"&gt;
	&lt;div class="b2 b2_m1"&gt;
		&lt;div class="b2\__e1"&gt;&lt;/div&gt;
		&lt;div class="b1\__e2 b1\__e2\_m2"&gt;&lt;/div&gt;
	&lt;/div&gt;
&lt;/div&gt;</code></pre>
</td>
</tr>

</table>

Remember that you can always make `bem` filter a default one for HTML syntax.

你可以让 HTML 语法默认启用 `bem` 过滤器。