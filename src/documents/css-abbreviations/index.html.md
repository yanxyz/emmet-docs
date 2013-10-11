---
layout: page
title: CSS 缩写
menuOrder: 2
---
While Emmet abbreviations are good for generating HTML, XML or any other structured markup, it may look useless for CSS. You don’t want to write CSS selectors and transform them to CSS selectors, right? The only thing Emmet can do for you is to provide shorthands for CSS properties, but editors with native snippets and autocomplete can help you way better.

Emmet 能很好的用于生成HTML、XML等结构语言，而对 CSS 似乎没用。你不想书写选择器然后将它们转化为选择器，对吧？（译注：意思是指对于选择器没有意义） Emmet 能做的只是提供 CSS 属性简写，而编辑器原生代码片断与自动补全帮助更大。

Actually, Emmet has something to offer.

实际上 Emmet 能做一些事。

For CSS syntax, Emmet has a lot of predefined snippets for properties. For example, you can expand `m` abbreviation to get `margin: ;` snippet. But you don’t want just `margin` property, you want to _specify a value_ for this property. So you have to manually type, let’s say, `10px`.

对于 CSS, Emmet 有大量预定义的属性代码片断。例如展开缩写 `m` 得到 `margin: ;`。但是你不只想得到 `margin`，你想给这个属性指定一个值，于是你手动输入，比如说 `10px`。

Emmet can greatly optimize your workflow here: you can _inject value directly into abbreviation_. To get `margin: 10px;` you can simply expand the `m10` abbreviation. Want multiple values? Use a hypen to separate them: `m10-20` expands to `margin: 10px 20px;`. Negative values? No problem: precede the first value with hyphen and all the rest with double hyphens: `m-10--20` expands to `margin: -10px -20px;`

这里 Emmet 能大大优化你的工作流程：将值直接注入缩写。为了得到 `margin: 10px;` 只用简单的展开缩写 `m10`。想要多个值？ 使用连字符分隔值：`m10-20` 展开为 `margin: 10px 20px;`。负值？没问题，第一个值前放一个连字符，其它的值前放两个连字符：`m-10--20` 展开为 `margin: -10px -20px;`。

## How it works? 工作原理

Emmet has a special CSS resolver that expands such abbreviations into a complete CSS property.

Emmet 使用特别的 CSS 解析器将缩写展开为完整的 CSS 属性。

Here’s what happens when you expand `m10` abbreviation.

下面是展开缩写 `m10` 的过程。

First, it looks for a `m10` snippet definition in `snippets.json`. If it’s found, it simply outputs it as a regular snippet. Otherwise, it _extracts value_ from abbreviation.

首先在 `snippets.json` 里查找定义 `m10` 。如果找到了则将它作为普通的代码片断输出。否则从缩写里提取值。

To provide best user experience, resolver doesn’t introduce any special value separator: it’s much faster to type `m5` rather than `m:5`. So it needs to find a value bound: *a first occurrence of digit or hyphen is treated as a value bound*. In `m10` example, `m` is _property part_ and `10` is _value part_.

为了提供最好的用户体验，解析器没有引入专门的值分隔符：输入 `m5` 比 `m:5` 快得多。这样需要查找值界定：最先出现的数字或连字符作为值界定。对于 `m10`来说， `m` 是属性，`10` 是值。

When property part is found, resolver searches for the snippet definition in `snippets.json`. For an `m` part, it will find `"m": "margin:|;"` definition (`|` character is used as a caret position reference when the snippet is expanded).

当找到属性部分后，解析器在 `snippets.json` 里查找代码片断定义。对于 `m` , 找到定义 `"m": "margin:|;"` （`|` 是缩写展开后的插入符位置）。

The snippet definition looks like a CSS property (this is very important!) so Emmet is able to split it to a CSS property and value and place transformed value part at caret position (the `|` character).

代码片断定义看着像 CSS 属性（这很重要！），这样 Emmet 能够将缩写分成属性与值两部分，并将转换后的值放到插入符的位置（由 `|` 指定）

## Supplying values with units 添加单位

By default, when you expand an abbreviation with integer value, Emmet outputs it with a `px` unit: `m10` → `margin: 10px;`. If you’re expanding an abbreviation with a float value, it is outputted with an `em` unit: `m1.5` → `margin: 1.5em;`. But you can explicitly provide the unit name, just by putting any alpha characters right after value: `m1.5ex` → `margin: 1.5ex;`, `m10foo` → `margin: 10foo;`.

当展开整数值时，Emmet 默认添加单位 `px`，例如 `m10` → `margin: 10px;`。如果是展开浮点数值，添加单位 `em`，例如 `m1.5` → `margin: 1.5em;`。不过可以显式地在值后面指定单位：`m1.5ex` → `margin: 1.5ex;`, `m10foo` → `margin: 10foo;`。

If you’re explicitly defining units, you don’t need to use hyphens to separate values anymore: `m10ex20em` → `margin: 10ex 20em;`, `m10ex-5` → `margin: 10ex -5px;`.

如果显式地指定单位，不再需要用连字号分隔值：`m10ex20em` → `margin: 10ex 20em;`, `m10ex-5` → `margin: 10ex -5px;`。

## Value aliases 单位别名

Emmet has a few aliases for commonly used values:

常用单位别名：

* `p` → `%`
* `e` → `em`
* `x` → `ex`

You can use aliases instead of full units:

示例：

* `w100p` → `width: 100%`
* `m10p30e5x` → `margin: 10% 30em 5ex`

## Color values 颜色值

Emmet supports hex color values, like this: `c#3` → `color: #333;`. The `#` sign is a _value separator_ so you don’t need to use hyphen to separate it. For example, `bd5#0s` expands to `border: 5px #000 solid`: the `#` sign separates color from `5` and since `s` (alias to `solid`) is not a hexadecimal character, it can be used without `-` value separator.

Emmet 支持 16 进制颜色值，例如：`c#3` → `color: #333;`。`#` 是值分隔符，所以不需要连字符。例如 `bd5#0s` 展开为 `border: 5px #000 solid`，`#` 将颜色值与 `5` 隔开，既然 `s` ( `solid` 的别名) 不是 16 进制字符，就不需要用连字符。

You can write one, two, three or six characters as color value:

可以写 1 个， 2 个，3 个或 6 个字符作为颜色值:

* `#1` → `#111111`
* `#e0` → `#e0e0e0`
* `#fc0` → `#ffcc00`

When `css.color.short` [preference](/customization/preferences/) is enabled (by default), color values like `#ffcc00` are automatically shortened to `#fc0`. You can also automatically change character case with `css.color.case` preference.

当在[配置](/customization/preferences/)中启用选项 `css.color.short` 后（默认启用），颜色值如 `#ffcc00` 自动简化为 `#fc0`。也可以用选项 `css.color.case` 自动改变颜色值字符的大小写。

## Unit-less properties 无单位属性

Some CSS properties are defined as _unit-less_, e.g. no unit suffix will be outputted: `lh2` → `line-height: 2;`, `fw400` → `font-weight: 400;`.

有些 CSS 属性无单位。例如： `lh2` → `line-height: 2;`, `fw400` → `font-weight: 400;`

These values are: `'z-index`, `line-height`, `opacity` and `font-weight` but you can override them with `css.unitlessProperties` preferences.

这些属性是：`'z-index`, `line-height`, `opacity` 和 `font-weight`。可以用选项 `css.unitlessProperties` 配置。

## !important modifier

You can add `!` suffix at the end of any CSS abbreviation to get `!important` value:

在任意 CSS 缩写后面添加 `!`，将得到 `!important` 值：

    p!+m10e!

...will produce

```css
padding:  !important;
margin: 10em !important;
```
