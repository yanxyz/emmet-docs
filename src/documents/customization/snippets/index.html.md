---
layout: page
title: "snippets.json"
menuOrder: 1
---
Create `snippets.json` file in extensions folder to add or override snippets. The structure of this file is the same as the [original one](https://github.com/emmetio/emmet/blob/master/snippets.json): on the top level you define _syntax name_ your snippets belong to, and the second level has the following section:

在扩展目录创建 `snippets.json` 文件，添加或覆盖代码片断。文件结构同[默认文件](https://github.com/emmetio/emmet/blob/master/snippets.json)，在顶层定义代码片断所属的语法名，次级的结构：

* `abbreviations` or `snippets` contains snippets definitions of [different types](/abbreviations/types/).
* `abbreviations` 与 `snippets` 包含[不同类型](/abbreviations/types/)的代码片断定义。
* `filters` contains a comma-separated list of [filters](/filters/) applied by default for current syntax. If this property is not defined, `html` filter is used.
* `filters` 包含一个逗号分割列表，用于指定应用于当前语法的[过滤器](/filters/)。如果没有指定，则使用 `html` 过滤器。
* `extends`: syntax name from which current syntax should inherit snippets definitions. For example, `sass` syntax is inherited from `css` one, but you can create your own or override some SASS-specific snippets for this syntax definition.
* `extends`: 指定当前语法继承哪个语法的代码片断。例如 `sass` 语法继承自 `css`，不过可以创建自己的或覆盖一些 SASS 专有的代码片断。

When loaded, users’ `snippets.json` in _recursively merged_ with the original one, adding or updating abbreviations and snippets.

当 Emmet 加载时，用户的 `snippets.json` 与默认文件合并，以添加或更新缩写与代码片断。

### Text snippets 文本代码片断

In `snippets` section of syntax definition, you create plain text snippets, pretty like the same as your editor ones. You can also use _tabstops_ inside snippets to traverse between them with Tab key when abbreviation is expanded (if your editor supports them). Emmet borrows tabstop format from [TextMate](http://macromates.com) editor:

在 `snippets` 部分创建文本代码片断。可以在代码片断名为使用插入占位，当缩写展开后可以用 Tab 键在这些插入占位之间移动（需要编辑器支持）。Emmet 借用了 [TextMate](http://macromates.com) 的格式：

* `$1` or `${1}`
* `${1:hello world}` — 有占位文本的插入占位

Note that `${0}` or `$0` tabstop has a special meaning in some editors like TextMate or Eclipse and is used as a final caret position after leaving “tabstops mode” so you’d better use tabstops staring from 1.

注意在一些编辑器如TextMate 或 Eclipse 下，`${0}` 与 `$0` 有特殊意义，用于指示离开插入占位模式后插入符最终位置，所以插入占位最好从 1 开始。

### Variables 变量

You can use _variables_ in snippets to output predefined data. For example, the `html:5` snippet of HTML syntax has the following definition:

可以在代码片断中使用变量，以输出预先定义的数据。例如 `html:5` 定义如下：

    <!doctype html>\n<html lang="${lang}">...</body>\n</html>

In the example above, `${lang}` is used to refer `lang` variable defined in `variables` section of `snippets.json`. If your primary language is, for example, Russian, you can simply override `lang` variable with `ru` value and keep the original snippets.

`${lang}` 引用 `snippets.json` 文件的 `variables` 部分下变量 `lang` 。如果你的主要语言，比如说俄语，只用将变量 `lang` 值改为 `ru`，而原代码片断不用变。

Also, you can override variable values with inline abbreviation attributes: `html:5[lang=ru]`. Together with ID and CLASS attributes shorthands—`#` and `.`—you can easily override variables right in abbreviation:

也可以用内联属性缩写覆盖变量值：`html:5[lang=ru]`。与 ID/CLASS 属性一起使用后，可以轻易的在缩写里覆盖变量值：

    "for": "for (var ${class} = 0; i < ${id}.length; ${class}++) {\n\t|}"

Example usage: `for#array.i`.

### Predefined variables 预定义变量

Snippets have some predefined variable names that have special meaning to Emmet:

Emmet 有下面预定义变量：

* `${cursor}` or `|` are synonyms to `$0` and used as caret position in generated output.
* `${cursor}` 与 `|` 同`$0`，指示当代码片断展开后插入符的位置。
* `${child}` refers to a position where child abbreviations and snippets should be outputted. If not defined, children will be outputted at the end of snippet content.
* `${child}` 指示子缩写或代码片断的位置。如果没有指定，它们将输出在代码片断末尾。

### Escaping `|` and `$` characters 转义`|` `$`

The `$` character is used for tabstops and variables, the `|` character it used to indicate caret position when snippet is expanded. If you want to output these characters as-is, you should use double slash to escape them: `\\$` or `\\|`

`$` 用于插入占位与变量，`|` 用于指示当代码片断展开后插入符的位置。如果想输出字面上的 `|` `$`，需要用双反斜杠转义：`\\$`  `\\|`。

### Sharing snippets 分享代码片断

If you want to share your snippets with other users, you should put them into a file which name starts with `snippets`, for example: `snippets-foo.json`, `snippets_bar.json`, `snippetsBaz.json`. Emmet will load them on start and merge into  a single snippets set.

如果你想分享你的代码片断给他人，将这些代码片断放在名字以 `snippets` 打头的文件内，比如 `snippets-foo.json`, `snippets_bar.json`, `snippetsBaz.json` ， Emmet 在启动时会加载它们并合并成一个代码片断集合。

_Notice that snippets defined in `snippets.json` file has higher priority over ones defined in `snippets*.json`_.

译注：原文错误。实际是 `snippets.json` 文件优先级最低。
