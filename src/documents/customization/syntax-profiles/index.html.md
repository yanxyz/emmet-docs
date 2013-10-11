---
layout: page
title: "syntaxProfiles.json"
menuOrder: 3
---
Output profiles are used to define how generated HTML content should look like. For example, when you expand `br` abbreviation, Emmet may produce one of the following tag:

输出配置用于定义如何输出 HTML 。例如当展开 `br` 缩写， Emmet 有下面几种输出：

* `<br>` — HTML notation
* `<br />` — XHTML notation
* `<br/>` — XML notation

Emmet tries to automatically detect output profile for current document. For example, if a document contains XHTML doctype, it will use `xhtml` profile, `html` otherwise.

Emmet 试着自动检测当前文档的输出配置。例如如果文档包含  XHTML doctype，则 Emmet 将使用 `xhtml` 配置，否则使用 `html` 配置。

But sometimes you’d like to force Emmet to use another profile for specified syntax or use your own profile with specific rules.

但是有时你想对特定语法强制 Emmet 使用另一种配置或者自定义配置。

In this case, you should create `syntaxProfiles.json` file in extensions folder and specify profile for a required syntax.

在这种情况下，在扩展目录下创建文件 `syntaxProfiles.json`，对目标语法指定配置。

The content of this file is a simple key–value dictionary where the key is the syntax name as defined in `snippets.json` and the value is a name of predefined profile (`String`) or a dictionary with profile options :

此文件内容是简单的字典键值对，键是 `snippets.json` 文件里的语法名，值是预定义配置名 (`String`) 或含有配置选项的字典(`Object`):

```javascript
{
    // force XHTML profile for HTML syntax
    "html": "xhtml",

    // create our own profile for XML
    "xml": {
        "tag_case": "upper",
        "attr_quotes": "single"
    }
}
```

### Predefined profiles 预定义配置

* `html` — default output profile.
* `html` — 默认配置
* `xhtml` — the same as `html`, but outputs empty elements with closed slash: `<br />`.
* `xhtml` — 同 `html`，不过在输出空标签时自关闭：`<br />`。
* `xml` — default for XML and XSL syntaxes: outputs each tag on a new line with indentation, empty elements are outputted with closing slash: `<br/>`.
* `xml` — XML 与 XSL 语法默认配置： 输出时每个标签一行并进行缩进，空标签自关闭`<br/>`。
* `line` — used to output expanded abbreviation without any indentation and newlines. In some editors applies by default in programming languages like JavaScript or Python to produce valid strings.
* `line` — 扩展缩写时不进行缩进或换行，在一些编辑器下默认应用于编程语言比如 JavaScript 或 Python，以输出正确的字符。

### Create your own profile 创建自己的配置

You can specify a dictionary with the following keys to create your own output profile:

用下面选项创建自己的配置：

* `tag_case`: case of generated tag name, string. Possible values are `upper`, `lower` and `asis`.
* `attr_case`: case of attribute names of generated tags, string. Possible values are `upper`, `lower` and `asis`.
* `attr_quotes`: quotes around attribute values, string. Possible values are `single` and `double`.
* `tag_nl`: output each tag on new line with indentation, boolean. Values are `true` (each tag on new line), `false` (no formatting) and `'decide'` (string; only block-level elements on new lines).
* `tag_nl_leaf`: with `tag_nl` set to `true`, defines whether leaf block-level node (e.g. node with no children) should have formatted line breaks inside.
* `indent`: indent tags on new lines, boolean.
* `inline_break`: how many inline elements are needed to force line break, number. The default value is `3`. For example, `span*2` will be expanded into `<span></span><span></span>`, but `span*3` will create three `<span>` elements, each on a new line. Set this option to `0` to disable line breaks for inline elements.
* `self_closing_tag`: should empty elements—like `br` or `img`—be outputted with closing dash, boolean. Values are `true`, `false` and `'xhtml'` (string; output closing slash in XHTML style, e.g. `<br />`).
* `filters`: list of [filters](/filters/) to be applied automatically.