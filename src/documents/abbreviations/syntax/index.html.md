---
layout: page
title: 缩写语法
menuTitle: 语法
menuOrder: 1
---
Emmet uses syntax similar to CSS selectors for describing elements’ positions inside generated tree and elements’ attributes.

Emmet 使用类似于 CSS 选择器的语法来描述元素的结构与属性。

## Elements  元素

You can use elements’ names like `div` or `p` to _generate_ HTML tags. Emmet doesn’t have a predefined set of available tag names, you can write any word and transform it into a tag: `div` → `<div></div>`, `foo` → `<foo></foo>` and so on.

使用元素的名字，比如 `div`、 `p` 来生成 HTML 标签。 Emmet 没有预定义标签集合，所以可以用任意单词来生成对应的标签：`div` → `<div></div>`, `foo` → `<foo></foo>`

## Nesting operators 嵌套操作符

Nesting operators are used to position abbreviation elements inside generated tree: whether it should be placed inside or near the context element.

### Child: `>` 子元素

You can use `>` operator to nest elements inside each other:

	div>ul>li

...will produce

	<div>
		<ul>
			<li></li>
		</ul>
	</div>

### Sibling: `+` 兄弟元素

Use `+` operator to place elements near each other, on the same level:

	div+p+bq

...will output

	<div></div>
	<p></p>
	<blockquote></blockquote>

### Climb-up: `^` 返回上层

With `>` operator you’re descending down the generated tree and positions of all sibling elements will be resolved against the most deepest element:

`>` 操作符加深结构层次：

	div+div>p>span+em

...will be expanded to

	<div></div>
	<div>
		<p><span></span><em></em></p>
	</div>

With `^` operator, you can climb one level up the tree and change context where following elements should appear:

`>` 操作符返回上一层：

	div+div>p>span+em^bq

...outputs to

	<div></div>
	<div>
		<p><span></span><em></em></p>
		<blockquote></blockquote>
	</div>

You can use as many `^` operators as you like, each operator will move one level up:

多个`^`连写将向上一层层返回：

	div+div>p>span+em^^^bq

...will output to

	<div></div>
	<div>
		<p><span></span><em></em></p>
	</div>
	<blockquote></blockquote>

### Multiplication: `*` 乘法

With `*` operator you can define how many times element should be outputted:

	ul>li*5

...outputs to

	<ul>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>

### Grouping: `()` 分组

Parenthesises are used by Emmets’ power users for grouping subtrees in complex abbreviations:

	div>(header>ul>li*2>a)+footer>p

...expands to

	<div>
		<header>
			<ul>
				<li><a href=""></a></li>
				<li><a href=""></a></li>
			</ul>
		</header>
		<footer>
			<p></p>
		</footer>
	</div>

If you’re working with browser’s DOM, you may think of groups as Document Fragments: each group contains abbreviation subtree and all the following elements are inserted at the same level as the first element of group.

可以将分组当作 Document Fragments，后续元素将与分组第一个元素同级。

You can nest groups inside each other and combine them with multiplication `*` operator:

分组嵌套，并且使用 `*` 操作法：

	(div>dl>(dt+dd)*3)+footer>p

...produces

	<div>
		<dl>
			<dt></dt>
			<dd></dd>
			<dt></dt>
			<dd></dd>
			<dt></dt>
			<dd></dd>
		</dl>
	</div>
	<footer>
		<p></p>
	</footer>

With groups, you can literally write full page mark-up with a single abbreviation, but please don’t do that.

使用分组后，可以用一个缩写来生成整个页面，不过不要这么做。

## Attribute operators 属性操作符

Attribute operators are used to modify attributes of outputted elements. For example, in HTML and XML you can quickly add `class` attribute to generated element.

### ID and CLASS

In CSS, you use `elem#id` and `elem.class` notation to reach the elements with specified `id` or `class` attributes. In Emmet, you can use the very same syntax to _add_ these attributes to specified element:

Emmet 使用类似于 CSS 选择器的语法给元素添加属性：

	div#header+div.page+div#footer.class1.class2.class3

...will output

	<div id="header"></div>
	<div class="page"></div>
	<div id="footer" class="class1 class2 class3"></div>

### Custom attributes 自定义属性

You can use `[attr]` notation (as in CSS) to add custom attributes to your element:

	td[title="Hello world!" colspan=3]

...outputs

	<td title="Hello world!" colspan="3"></td>

* You can place as many attributes as you like inside square brackets.
* 方括号内属性数量不限。
* You don’t have to specify attribute values: `td[colspan title]` will produce `<td colspan="" title="">` with tabstops inside each empty attribute (if your editor supports them).
* 没有指定值的属性将生成插入占位（需要编辑器支持）。
* You can use single or double quotes for quoting attribute values.
* 属性值使用单引号或双引号。
* You don’t need to quote values if they don’t contain spaces: `td[title=hello colspan=3]` will work.
* 属性值如果不包含空格可以省略引号。

### Item numbering: `$` 编号

With multiplication `*` operator you can repeat elements, but with `$` you can _number_ them. Place `$` operator inside element’s name, attribute’s name or attribute’s value to output current number of repeated element:

`*` 操作符可以生成重复元素，而 `$` 可以对元素编号。将 `$` 放在元素名、属性名或属性值中：

	ul>li.item$*5

...outputs to

	<ul>
		<li class="item1"></li>
		<li class="item2"></li>
		<li class="item3"></li>
		<li class="item4"></li>
		<li class="item5"></li>
	</ul>

You can use multiple `$` in a row to pad number with zeroes:

多个连写的 `$` 可以生成带有前导零的编号：

	ul>li.item$$$*5

...outputs to

	<ul>
		<li class="item001"></li>
		<li class="item002"></li>
		<li class="item003"></li>
		<li class="item004"></li>
		<li class="item005"></li>
	</ul>

#### Changing numbering base and direction

With `@` modifier, you can change numbering direction (ascending or descending) and base (e.g. start value).

使用 `@` 修饰符，可以改变编号的方向（升序或降序）及起点。

For example, to change direction, add `@-` after `$`:

例如改变方向，将 `@-` 放在 `$` 后：

	ul>li.item$@-*5

…outputs to

	<ul>
		<li class="item5"></li>
		<li class="item4"></li>
		<li class="item3"></li>
		<li class="item2"></li>
		<li class="item1"></li>
	</ul>

To change counter base value, add `@N` modifier to `$`:

改变起点，将 `@N` 放在 `$` 后：

	ul>li.item$@3*5

…transforms to

	<ul>
		<li class="item3"></li>
		<li class="item4"></li>
		<li class="item5"></li>
		<li class="item6"></li>
		<li class="item7"></li>
	</ul>

You can use these modifiers together:

混合使用这几种修饰符：

	ul>li.item$@-3*5

…is transformed to

	<ul>
		<li class="item7"></li>
		<li class="item6"></li>
		<li class="item5"></li>
		<li class="item4"></li>
		<li class="item3"></li>
	</ul>

## Text: `{}` 文本

You can use curly braces to add text to element:

使用大括号为元素添加文本（译注：类似于模板的插入符）

	a{Click me}

...will produce

	<a href="">Click me</a>

Note that `{text}` is used and parsed as a separate element (like, `div`, `p` etc.) but has a special meaning when written right after element. For example, `a{click}` and `a>{click}` will produce the same output, but `a{click}+b{here}` and `a>{click}+b{here}` won’t:

注意 `{text}` 类似于独立元素（比如`div`, `p`），不过当它紧跟在元素后面时有特别的意义。比如 `a{click}` 与 `a>{click}` 结果一样，而 `a{click}+b{here}` 与 `a>{click}+b{here}` 结果不一样：

	<!-- a{click}+b{here} -->
	<a href="">click</a><b>here</b>

	<!-- a>{click}+b{here} -->
	<a href="">click<b>here</b></a>

In second example the `<b>` element is placed _inside_ `<a>` element. And that’s the difference: when `{text}` is written right after element, it doesn’t change parent context. Here’s more complex example showing why it is important:

第二个例子里 `<b>` 位于 `<a>` 内。这便是不同点： 当 `{text}` 紧跟在元素后面时，它没有改变父元素的上下文。下面用一个复杂例子来说明：

	p>{Click }+a{here}+{ to continue}

...produces

	<p>Click <a href="">here</a> to continue</p>

In this example, to write `Click here to continue` inside `<p>` element we have explicitly move down the tree with `>` operator after `p`, but in case of `a` element we don’t have to, since we need `<a>` element with `here` word only, without changing parent context.

在这个例子中，为了让 `<p>` 包含 `Click here to continue`，`p` 后面使用了 `>` 以进入子级结构，而 `a` 只需要包含文本 `here`，不用改变父元素上下文，所以不需要这样做。

For comparison, here’s the same abbreviation written without child `>` operator:

下面不用 `>` 做下对比：

	p{Click }+a{here}+{ to continue}

...produces

	<p>Click </p>
	<a href="">here</a> to continue

## Notes on abbreviation formatting 格式化缩写注意事项

When you get familiar with Emmet’s abbreviations syntax, you may want to use some formatting to make your abbreviations more readable. For example, use spaces between elements and operators, like this:

当熟悉 Emmet 的缩写语法后，你可能为了可读性而去格式化缩写。比如在元素与操作符之间插入空格：

	(header > ul.nav > li*5) + footer

But it won’t work, because space is a _stop symbol_ where Emmet stops abbreviation parsing.

但是这时 Emmet 失效，因为 Emmet 遇到空格后停止解析缩写。

Many users mistakenly think that each abbreviation should be written in a new line, but they are wrong: you can type and expand abbreviation *anywhere in the text*:

许多用户错误地认为缩写应该新起一行，但是这是错的：可以在文本的任意位置书写并展开缩写。

<textarea class="movie-def">
&lt;body&gt;
	|
&lt;/body&gt;
~~~
type: ul#nav>li*4
wait: 1000
run: emmet.expand_abbreviation
wait: 1000
type: Hello world span.info
wait: 1000
tooltip: You don’t need new line to expand abbreviation
wait: 600
run: emmet.expand_abbreviation
wait: 1000
moveTo: 87
wait: 1500
type: span.info
wait: 1000
tooltip:{text: "Emmet is smart enough to understand that you’re trying to expand <strong>span.info</strong> abbreviation, not the <strong>li>span.info</strong> one", wait: 5000}
run: emmet.expand_abbreviation
</textarea>

This is why Emmet needs some indicators (like spaces) where it should stop parsing to not expand anything that you don’t need. If you’re still thinking that such formatting is required for complex abbreviations to make them more readable:

这便是为什么 Emmet 需要指示符（比如空格）来停止解析缩写。如果你仍然认为对于复杂的缩写，为了可读性必须格式化：

* Abbreviations are not a template language, they don’t have to be “readable”, they have to be “quickly expandable and removable”.
* 缩写不是模板语言，不需要可读性，即写即用。
* You don’t really need to write complex abbreviations. Stop thinking that “typing” is the slowest process in web-development. You’ll quickly find out that constructing a single complex abbreviation is much slower and error-prone than constructing and typing a few short ones.
* 你真的没必要书写复杂的缩写。停止这样的认识：书写是网页开发中最慢的过程。你将很快发现书写一个复杂的缩写比起使用多个简短缩写，要慢得多并且容易出错。