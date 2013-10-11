---
layout: page
title: 渐变
menuOrder: 2
---
Another hard-to-write CSS3 feature is a gradient. You have to repeat long gradient definition multiple times with different vendor prefixes. Also, if you want to cover all gradient-supported browsers, you have to use three different notations: old Webkit, currently supported (`linear-gradient(top, ...)`) and W3C-proposed (`linear-gradient(to bottom, ...)`).

另一个难写的 CSS3 特性是渐变，需要重复写几遍带有不同厂商前缀的属性。而且如果想覆盖所有支持渐变的浏览器，得使用三种写法：旧版 Webkit、当前支持的 (`linear-gradient(top, ...)`) 及 W3C 标准 (`linear-gradient(to bottom, ...)`)。

译注：查看目前的[兼容性](https://developer.mozilla.org/en-US/docs/Web/CSS/linear-gradient)

Usually, users prefere to use third-party GUIs to generate gradients definitions, but you can do the very same thing much faster right in your editor.

通常用户喜欢使用第三方 GUI 程序来生成渐变，但是在编辑器里面做得更快。

Emmet has a CSS3 Gradient Generator that can do all the hard work for you:

Emmet 有一个 CSS3 渐变生成器替你做这些重活：

<textarea class="movie-def">
div {
	|
}
@@@
tooltip: Type normal CSS Gradient definition as <strong>lg(...)</strong> inside CSS rule
type: lg(left, #fc0 30%, red)
wait: 1000
tooltip: Run “Expand Abbreviation” action to transform gradient definition ::: “Expand Abbreviation” (Tab key)
run: emmet.expand_abbreviation
wait: 1000
moveTo: 5:59
run: {command: "emmet.insert_formatted_line_break", times: 2}
wait: 500
type: border-image:
tooltip: If you write <strong>lg(...)</strong> definition as property value, Emmet will inherit its property name
type: lg(left, #fc0 30%, red)
wait: 500
run: emmet.expand_abbreviation
wait: 1000
moveTo: 11:50
select: 11:53
tooltip: {text: "You can modify generated gradient definition and run “Expand Abbreviation” action again to mirror changes to other gradients with the same CSS property name", wait: 7000}
type: black
wait: 500
run: emmet.expand_abbreviation
@@@
mode: text/css
</textarea>

As you can see from the example above, you can type regular gradient definition as `lg(...)` (or `linear-gradient(...)`) function and expand it as an abbreviation. If you write the gradient definition as a property value, Emmet will parse it and use its name as a reference for new CSS properties.

如你所见，可以输入函数 `lg(...)` (或 `linear-gradient(...)`) 函数，并且像缩写一样展开。如果用做属性值，Emmet 将使用属性名来生成新的属性。

## Fallback value 向后兼容

In preferences, you can enable `css.gradient.fallback` option to produce a fallback `background-color` CSS property whenever a gradient definition for `background-*` CSS property is expanded. This fallback property will contain a first color from gradient definition.

在配置里启用选项 `css.gradient.fallback` 后可以生成向后兼容的 `background-color`。

This option is off by default because it produces a `background-color` value that almost certainly needs to be manually updated to make sure that content is readable on this background. If you don’t really care about old browsers, you can enable this option.

这个选项默认关闭，因为它生成的 `background-color` 总是需要手工更新，以确保在这个背景色上可以阅读。如果你不关心旧浏览器，可以启用这个选项。