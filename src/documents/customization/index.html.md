---
layout: page
title: 配置
menuOrder: 5
---
Emmet offers wide range of tweaks you can use to fine-tune your plugin experience. Almost all officially developed editor plugins (except PSPad and browser-based) has **extensions support**: a special folder where you can put `json` and `js` files to extend Emmet. Please refer to README file bundled with your editor’s plugin to find out where Emmet looks for extensions.

几乎所有的官方开发的插件（除了 PSPad 与 网页编辑器的插件外）均支持扩展： 将 `json` 与 `js` 文件放到特定目录下。请查看你的编辑器插件说明，找到这个目录。

译注：这里所说的插件即 Emmet。

Each `.js` file located in extensions folder will be loaded and executed on plugin start-up. Use `js` files to create your own [filters](/filters/) or [actions](/actions/): you can use Emmet modules and bindings to script your editor with JavaScript.

扩展目录下所有的 `.js` 文件在插件启动时加载并执行。使用 `.js` 文件创建你自己的 [过滤器](/filters/) 或 [功能](/actions/)：你可以利用 Emmet 的模块与绑定，以 JavaScript 来编写你的编辑器插件。

With `.json` files you can fine-tune different parts of Emmet toolkit:

使用 `.json` 文件配置 Emmet：

<dl>
	<dt>[snippets.json](./snippets/)</dt>
	<dd>Add your own or update existing snippets.</dd>
    <dd>添加或更新已有的代码片断。</dd>
	<dt>[preferences.json](./preferences/)</dt>
	<dd>Change behavior of some Emmet filters and actions.</dd>
    <dd>配置过滤器与功能。</dd>
	<dt>[syntaxProfiles.json](./syntax-profiles/)</dt>
	<dd>Define how generated HTML/XML should look.</dd>
    <dd>定义怎样输出 HTML/XML。</dd>
</dl>

## 译注

在Sublime Text 下 Emmet 可以用选项 `extensions_path` 配置扩展目录，默认为 `~/emmet`。也可以用相对路径，对于便携版，是相对于 `sublime_text.exe` 的路径。