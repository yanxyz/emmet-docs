---
layout: page
title: 模糊查找
menuOrder: 3
---
If you take a look at [Cheat Sheet](/cheat-sheet/), you’ll find that there are too many CSS snippets to remember. Also, some of them might be a bit lengthy for sake of logical separation.

看一看 [速查表](/cheat-sheet/)，会发现要记的 CSS 代码片断太多了。一些也可能有点长。

To make CSS writing a bit easier, Emmet implement _fuzzy search_ logic for CSS snippets: every time you enter unknown abbreviation, Emmet will try to find a closest snippet definition.

为了让书写 CSS 更容易， Emmet 实现了模糊查找。每次输入未知的缩写时，Emmet 尝试查找最相近的代码片断。

For example, instead of writing `ov:h` (`overflow: hidden;`) abbreviation, you can write `ov-h`, `ovh` or even `oh`. You can play around with the fuzzy search in text editor below. Try to find as many variations as possible (use Tab key to expand abbreviations) for `bxz:cb`, `ovx:h` and `pos:a` snippets.

例如，缩写不是 `ov:h`(`overflow: hidden;`) ，而是 `ov-h`, `ovh` 甚至 `oh`。可以在下面文本框内试试。

<textarea class="cm-box" data-height="150" data-cm-mode="text/css"></textarea>

The fuzzy search is performed against _predefined snippet names_, not snippet values or CSS properties. This results in more predictable and controllable matches. Remember that you can always [create your own snippets or redefine existing ones](/customization/) to fine-tune fuzzy search experience.

模糊查找搜索代码片断名，而不是值或 CSS 属性，这样对可以控制匹配。记住可以[创建自己的或覆盖已有的代码片断](/customization/) ，以改进模糊查找的体验。