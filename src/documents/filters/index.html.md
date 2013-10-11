---
layout: page
title: 过滤器
menuOrder: 4
---
Filters are special post-processors that modify expanded abbreviation right before output to the editor. To better understand how filters work, let’s walk through a simple tutorial.

过滤器在输出发给编辑器之前修改缩写的展开结果。为了更好的理解过滤器是怎样工作的，下面讲一个简单例子。

Try to expand the following abbreviation in the editor below (use Tab key to expand abbreviation): `#content>p.title`

在编辑器里展开缩写：`#content>p.title`

<textarea class="cm-box" data-height="150"></textarea>

As you may expect, it will be expanded into the following HTML code:

	<div id="content">
		<p class="title"></p>
	</div>

Now, try to expand this abbreviation: `#content>p.title|e`. You’ll have a slightly different result:

再展开这个缩写：`#content>p.title|e`，结果有点不同：

```xml
&lt;div id="content"&gt;
	&lt;p class="title"&gt;&lt;/p&gt;
&lt;/div&gt;
```

We’ve just applied `e` (escape) filter by appending its name after pipe character. This filter had escaped all XML-unsafe symbols with entities right before Emmet sent output to the editor. Now, try this one:  `#content>p.title|e|e`:

这里使用了 `e` (escape) 过滤器，将过滤器名字放在管道符后面。这个过滤器在 Emmet 将输出发送给编辑器之前把所有 XML 不安全字符转换为实体。试试这个：`#content>p.title|e|e`

```xml
&amp;lt;div id="content"&amp;gt;
	&amp;lt;p class="title"&amp;gt;&amp;lt;/p&amp;gt;
&amp;lt;/div&amp;gt;
```

We have a double-escaped code (e.g. we’ve applied `e` filter twice). As you can see, we can apply as many filters to abbreviation as we want, and as many times as we want.

代码被双重转义。如你所见，可以对缩写使用多个过滤器，或多次使用。

Let’s do something more interesting. Try to expand this abbreviation: `#content>p.title|haml`

来点更有意思的。展开这个缩写：`#content>p.title|haml`

	#content
		%p.title

Isn’t it nice? We've just expanded abbreviation as a HAML template!

是不是不错？缩写展开为 HAML 模板！

As you can see, filtering is a key concept of Emmet. To draw an analogy with the browser’s DOM model, every time you expand abbreviation it first gets transformed into a tree and then filter walks on each tree node and modifies its output. Filters can do anything: from small tweaks as placing whitespace after CSS-rule to more complex tasks as outputting result in different syntax. Even HTML output is defined as `html` filter.

如你所见，过滤是 Emmet 的一个关键概念。类似于浏览器 DOM 树，缩写先转换为树，然后过滤器遍历树的节点，修改输出。过滤器能做任何事： 小到 CSS 规则是否放空格，大到复杂的任务，例如以不同的语法输出，即使 HTML 定义使用 `html` 过滤器。

## Implicit filter call 隐式地使用过滤器

You can apply filter to abbreviation explicitly, by adding pipe character and its name right after abbreviation. But filters also can be applied implicitly, depending on document type you're currently editing. You don’t want to append `|haml` every time you expand abbreviation in HAML document, right?

可以显式地使用过滤器，将过滤器名字与管道符放在缩写后面。也可以隐式地使用过滤器，这取决于当前文档的类型。你不想在 HAML 文件下每次展开缩写时都添加 `|haml` 吧？

Default filters are defined in [snippets.json](https://github.com/emmetio/emmet/blob/master/snippets.json) file in `filters` section of each syntax:

在 [snippets.json](https://github.com/emmetio/emmet/blob/master/snippets.json) 文件 `filters` 处为语法定义默认的过滤器：

	{
		...
		"html": {
			...
			"filters": "html"
		}
	}

If there’s no such section, `html` filter is applied by default. If you want to apply more than one filter by default, you can write a comma- or pipe-separated list of filter names in `filters` section:

如果没有，默认使用 `html` 过滤器。如果想使用多个过滤器，则指定一个列表，用逗号或管道符分隔过滤器的名字：

	{
		...
		"html": {
			...
			"filters": "html, e"
		}
	}

Now, every time you expand abbreviation in HTML document, `html` and `e` filters will be applied by default.

这样之后在 HTML 文档下展开缩写时，将默认使用 `html` 与 `e` 过滤器。

**But be careful!** You always have to place one of the syntax filter—`html` or `haml`—at first place of default filters in `snippets.json` file, otherwise you’ll have empty output because syntax filters are defining primary output result.

**注意！**必须将语法过滤器 `html` 或 `haml` 放在第一位。否则输出为空，因为语法过滤器定义主要的输出。

## Available filters 可用过滤器

### HAML syntax: `haml`
HAML syntax filter: output abbreviation as HAML template. Applies by default for HAML files.

HAML 语法过滤器：缩写输出为 HAML 模板，默认应用于HAML 文件。

### HTML syntax: `html`
HTML syntax filter: outputs abbreviation as HTML/XML tags. Applies by default everywhere except HAML files.

HTML 语法过滤器：缩写输出为 HTML/XML 标签，默认应用于除了 HAML 文件之外的所有地方。

### Escape: `e` 转义
Escapes XML-unsafe characters: `<`, `>` and `&`.

转义 XML 不安全字符：`<`, `>` 和 `&`。

For example, `div#header|e` will be expanded into `&lt;div id="header"&gt;&lt;/div&gt;`. This filter will be extremely useful for tech bloggers/writers who wants to show code snippets on website (if you add Emmet support into you CMS, of course).

例如 `div#header|e` 展开为 `&lt;div id="header"&gt;&lt;/div&gt;`。当科技博客或作者想在网站上展示代码时，这个过滤器就非常有用（当然要在 CMS 里添加 Emmet 支持）。

### Comment tags: `c` 注释
Add comments around important tags. By default, “important tags” are those tags with `id` and/or `class` attribute.

为重要标签添加注释。“重要标签”默认为有 `id` 或 `class` 属性的标签：

	div>div#page>p.title+p|c

...will be expanded into

	<div>
		<div id="page">
			<p class="title"></p>
			<!-- /.title -->
			<p></p>
		</div>
		<!-- /#page -->
	</div>

This filter has a number of [preferences](/customization/preferences/) you can re-define:

这个过滤器有若干[配置](/customization/preferences/)：

* `filter.commentTrigger`: list of attributes that should trigger comment output. Default value is `id, class`
* `filter.commentTrigger`: 触发注释的属性列表。默认值 `id, class`
* `filter.commentAfter`: a [ERB-style template](http://underscorejs.org/#template) of comment that should be placed right _after_ “important tag”. Default value is `\n<!-- /<%= attr("id", "#") %><%= attr("class", ".") %> -->`
* `filter.commentAfter`: 对于 [ERB 风格模板](http://underscorejs.org/#template)，注释应当放在“重要标签”之后，默认值 `\n<!-- /<%= attr("id", "#") %><%= attr("class", ".") %> -->`
* `filter.commentBefore`: 对于 ERB 风格模板，注释应当放在“重要标签”之前，默认值为空。

### XSL tuning: `xsl`
This filter removes `select` attribute from `<xsl:variable>` and `<xsl:with-param>` tags _if they have child nodes_. For example:

当 `<xsl:variable>` 与 `<xsl:with-param>` 标签有子节点时这个过滤器将移除它们的 `select` 属性。例如：

	ap>wp

will be expanded into

	<xsl:apply-templates select="" mode="">
		<xsl:with-param name="" select=""/>
	</xsl:apply-templates>

But

	ap>wp>call

...will be expanded into

	<xsl:apply-templates select="" mode="">
		<xsl:with-param name="">
			<xsl:call-template name=""/>
		</xsl:with-param>
	</xsl:apply-templates>

Applies by default in XSL files.

XSL 文件默认使用。

### Single line: `s` 单行

Outputs transformed abbreviation as a single line of code. Useful for writing template strings in programming languages like JavaScript, Python, Ruby etc. For example:

将缩写输出为单行。对书写 JavaScript, Python, Ruby 等编程语言比较有用，例如：

`ul>li*4|s`

...will be expanded into

	<ul><li></li><li></li><li></li><li></li></ul>

### Trim line markers: `t` 删除行标记

Useful for wrapping abbreviations only: removes line markers from wrapped lines, as described in “[Wrap with Abbreviation](/actions/wrap-with-abbreviation/)” action.

只对包装缩写有用： 说明见“[包装缩写](/actions/wrap-with-abbreviation/)”功能。