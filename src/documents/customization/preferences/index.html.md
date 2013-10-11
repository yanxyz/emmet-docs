---
layout: page
title: "preferences.json"
menuOrder: 2
---
The `preferences.json` file is used to modify behavior of some actions and resolvers of Emmet. This file contains a simple dictionary of key–value pairs.

`preferences.json` 文件用于配置 Emmet 的功能与解析器。

For example, on “[CSS Gradients](/css-abbreviations/gradients/)” there’s description of `css.gradient.fallback` option which enables fallback `background-color` value when definition is expanded. To enable it, simply add this key to `preferences.json` file:

例如 “[CSS Gradients](/css-abbreviations/gradients/)” 有一选项 `css.gradient.fallback`，用于启用兼容的 `background-color`：

    {
        "css.gradient.fallback": true
    }

Here’s a list of currently available options:

可用选项：

<div class="emmet-preferences"></div>
