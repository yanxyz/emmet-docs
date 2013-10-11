---
layout: page
title: 元素类型
menuOrder: 2
---
in HTML and XML documents, when you expand abbreviations, all abbreviation parts are transformed on-the-fly into HTML/XML tags. But certain elements like `a` or `img` are transformed into elements with predefined attributes: `<a href=""></a>` and `<img src="" alt="" />`. How does Emmet know when to add those attributes?

当编辑 HTML/XML 文档时，缩写展开为 HTML/XML 标签。不过一些元素，比如 `a` 或 `img`， 缩写展开后带有属性：`<a href=""></a>` 或 `<img src="" alt="" />`。Emmet 怎么知道何时添加这些属性？

All Emmet elements definitions are stored in [snippets.json](https://github.com/emmetio/emmet/blob/master/snippets.json) file in the following format:

Emmet 所有元素的定义放在 [snippets.json](https://github.com/emmetio/emmet/blob/master/snippets.json) 文件里，格式如下：

	{
		"html": {
			"abbreviations": {
				"a": "<a href=\"\">",
				"link": "<link rel=\"stylesheet\" href=\"\" />"
				...
			},
			"snippets": {
				"cc:ie6": "<!--[if lte IE 6]>\n\t${child}|\n<![endif]-->"
				...
			}
		},

		"css": {
			...
		}
	}

As you can see, at first level there are syntax names for which elements are defined. Inside the syntax section there are elements definitions split across two sections: _snippets_ and _abbreviations_.

如你所见，第一级是元素所属语法名，其中元素定义分成两部分： 代码片断与缩写。

## Snippets 代码片断

Snippets are just blocks of plain code, just like in all programmers’ editors. You can type anything there and it will be outputted “as-is”, without any transformation.

代码片断，同其它程序编辑器一样，是文本代码块，所见即所得，没有转化操作。

## Abbreviations 缩写

Abbreviations are actually building blocks with some data hints. Since Emmet is mostly used for writing HTML/XML tags, _abbreviation definition uses XML format to describe element_.

缩写是带有数据提示的代码块。既然 Emmet 主要用于编辑 HTML/XML， 于是缩写的定义使用 XML 格式来描述元素。

Emmet parses abbreviation definition and retrieves the following data:

Emmet 解析缩写的定义并获取下面数据：

* element name 元素名字;
* default attributes 默认属性;
* attributes’ order 属性顺序;
* attributes’ default values 属性默认值;
* should element contain closing tag 元素是否包含关闭标签.

Let’s take a closer look on HTML abbreviations’ definitions above. The `link` element is defined as `<link rel="stylesheet" href="" />` (double quotes should be escaped in JSON; or use single quotes instead). This definition says that tag, generated for `link` abbreviation, should be named _link_ and should contain two attributes: _rel_ with default value “ and _href_ with empty value (exactly in this order), and generated element should not contain closing tag.

拿上面的例子来说明。`link` 元素定义为 `<link rel="stylesheet" href="" />` （JSON 中需要转义双引号，或者用单引号）。这个定义的意思是，缩写 `link` 展开后元素带有两个属性： _rel_ 默认值stylesheet”；_href_ 空值，它们的顺序依照定义，元素不包含关闭标签。

When the `link` abbreviation is expanded, you’ll receive the following output for HTML syntax:

展开结果：

	<link rel="stylesheet" href="">

You can override default attribute values and add new ones as well:

可以覆盖默认值或添加一个新属性：

	link[rel=prefetch title="Hello world"]

...expands to:

	<link rel="prefetch" href="" title="Hello world">

You can add child elements as well, which forces Emmet to output closing tag:

也可以添加子元素，这将强制 Emmet 输出关闭标签：

	link>xsl:apply-templates

...will output:

	<link rel="stylesheet" href="">
		<xsl:apply-templates></xsl:apply-templates>
	</link>

## Aliases 别名

In the abbreviations section of `snippets.json` you can also define _aliases_: a short-hands for commonly used abbreviations. Aliases can be used to define:

在 `snippets.json` 文件的缩写部分，可以定义别名，作用是：

* short names for long tag names 给长标签名起一个短名字;
* referencing commonly used abbreviations 引用常用的缩写.

In `snippets.json` file, you can find the following definitions:

在`snippets.json` 文件里可以看到：

	...
	"html": {
		"abbreviations": {
			"bq": "blockquote",
			"ol+": "ol>li"
		}
	}

In the example above, when you expand `bq` abbreviation, Emmet will look for `blockquote` abbreviation’s definition. If it doesn’t exist, it will simply output `<blockquote></blockquote>` element. The `ol+` abbreviation actually outputs the same result as `ol>li` does.

在这个例子中，当展开缩写 `bq` 时，Emmet 查找 `blockquote` 的定义。如果定义不存在，则只输出 `<blockquote></blockquote>`。`ol+` 输出结果同 `ol>li`。

The `ol+` definition may look ambiguous since it contains `+` at the end which is also a sibling operator. Emmet correctly expands such abbreviations and the plus sign is left here for historical reasons. Just remember that you don’t need to use plus sign to create abbreviation alias.

`ol+` 看着有点懵，因为 `+` 也是兄弟操作符。Emmet 能正确的展开这样的缩写，这里的加号是历史缘故。记住，不需要用加号来定义缩写别名。
