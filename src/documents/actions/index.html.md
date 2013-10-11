---
layout: page
title: 功能
menuOrder: 3
---
Emmet allows you to write large HTML code blocks at speed of light using well-known CSS selectors. But it’s not the only thing that every web-developer needs: occasionally you have to _edit_ your HTML and CSS code to fix bugs and add new features.

Emmet 能让开发者以光速 :-) 书写大段的 HTML。但是这不是开发者唯一想要的：有时需要编辑 HTML 与 CSS 代码，以修订 bug 和添加新功能。

Emmet offers very unique tools that can greatly improve your editing experience:

Emmet 提供独有的工具，可以极大的提高你的编辑体验：

<dl>
<dt>[Expand Abbreviation 展开缩写](./expand-abbreviation/)</dt>
<dd>Yep, this is _the_ action that expands CSS-like abbreviations into HTML code.</dd>
<dd>将类似于 CSS 的缩写展开为 HTML 代码。</dd>

<dt>[Match Tag Pair 匹配标签](./match-pair/)</dt>
<dd>Selects content, and/or opening and closing HTML tag name from current caret position (a.k.a “balancing”). Super-awesome implementation that _works even in non-HTML syntaxes_! Implicitly used by many Emmet actions.</dd>
<dd>从插入符所在的位置选择标签内外内容。更厉害的是在非 HTML 语法下也能使用。Emmet 多数功能隐式的用到此功能。</dd>

<dt>[Go to Matching Pair 跳转到配对标签](./go-to-pair/)</dt>
<dd>Quickly traverses between opening and closing HTML tag.</dd>
<dd>在 HTML 标签的开始与关闭标记间跳转。</dd>

<dt>[Wrap with Abbreviation 包裹缩写](./wrap-with-abbreviation/)</dt>
<dd>Same as “Expand Abbreviation” action but intelligently wraps selected content.</dd>
<dd>同“展开缩写”功能，不过可以智能的包裹选中的内容。</dd>

<dt>[Go to Edit Point 跳转编辑点](./go-to-edit-point/)</dt>
<dd>Quickly traverse between important HTML code points.</dd>
<dd>在重要的 HTML 编辑点间移动</dd>

<dt>[Select Item 选择](./select-item/)</dt>
<dd>Quickly select important HTML and CSS code parts.</dd>
<dd>快速选择 HTML 与 CSS 代码片断。</dd>

<dt>[Toggle Comment 切换注释](./toggle-comment/)</dt>
<dd>Toggles comment. Unlike basic editor’s implementations, matches HTML tag, CSS property or rule when there’s no selection.</dd>
<dd>不同于编辑器的实现，如果没有选择，则对匹配的 HTML 标签， CSS 属性或规则切换注释。</dd>

<dt>[Split/Join Tag 分割合并标签](./split-join-tag/)</dt>
<dd>Splits (`<tag />` → `<tag></tag>`) or joins (`<tag></tag>` → `<tag />`) HTML/XML tag under current caret position.</dd>
<dd>将插入符所在的 HTML/XML 标签分割 (`<tag />` → `<tag></tag>`) 或合并 (`<tag></tag>` → `<tag />`)。</dd>

<dt>[Remove Tag 删除标签](./remove-tag/)</dt>
<dd>Gracefully removes HTML/XML tag under current caret position.</dd>
<dd>删除插入符所在的 HTML/XML 标签。</dd>

<dt>[Merge Lines 合并行](./merge-lines/)</dt>
<dd>Merges selected lines into single one. With no selection, automatically matches nearest HTML tag.</dd>
<dd>将选中的多行合并为单行。如果没有选择，则自动将最近的 HTML 标签合并。</dd>

<dt>[Update Image Size 更新图片尺寸](./update-image-size/)</dt>
<dd>Updates matched HTML tag or CSS rule with image size, located under caret.</dd>
<dd>更新插入符所在的图片(img 标签或 background 等 CSS 属性）的尺寸。</dd>

<dt>[Evaluate Math Expression 计算数学表达式](./evaluate-math/)</dt>
<dd>Evaluates simple math expression</dd>
<dd>计算简单的数学表达式。</dd>

<dt>[Increment/Decrement Number 增减数字](./inc-dec-number/)</dt>
<dd>Increments or decrements number under current caret position with given step.</dd>
<dd>以给定步值增减插入符所在的数字。</dd>

<dt>[Reflect CSS Value 重构 CSS 值](./reflect-css-value/)</dt>
<dd>Automatically copies CSS value under current caret position to all vendor-prefixed variants.</dd>
<dd>自动将插入符所在的 CSS 属性值复制给所有带有厂商前缀的属性。</dd>

<dt>[Encode/Decode Image to data:URL  编码/解码图像为 data:URL](./base64/)</dt>
<dd>Encodes image under caret to data:URL format and vice versa.</dd>
<dd>将插入符所在的图片编码为 data:URL， 或逆操作。</dd>

</dl>

**译注:** 查看在 Sublime Text 下各功能的[快捷键](https://github.com/sergeche/emmet-sublime#available-actions)。
