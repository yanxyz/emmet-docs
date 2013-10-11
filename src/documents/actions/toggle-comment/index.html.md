---
layout: page
title: 切换注释
menuOrder: 6
---
This action, as name says, toggle comment on selection. Almost all programmer’s text editors have such action, but this one works differently. When there’s no selection, editor’s action toggles comment on current line while Emmet’s one do this on _current context_. For HTML it’s a full tag, for CSS it’s a rule or full property.

这个功能，如名字所示，注释或取消注释选中内容。几乎所有的程序员编辑器都有这样的功能，但是这个不同。当没有选择时，编辑器切换当前行的注释，而 Emmet 切换当前上下文的注释。对于 HTML 是整个标签内容，对于 CSS 是一条规则或整个属性。

<textarea class="movie-def">
&lt;sty|le&gt;
body {
	padding: 10px; color: black;
}
&lt;/style&gt;
@@@
tooltip: {text: 'When invoked with no selection in HTML document, “Toggle Comment” action matches full tag', wait: 7000}
wait: 500
run: {command: 'emmet.toggle_comment', times: 2, beforeDelay: 1000} ::: “Toggle Comment” (Cmd-/)
wait: 1000
moveTo: 1:3
wait: 1000
tooltip: In CSS, it toggles comment on rule or full property, depending on caret position
run: {command: 'emmet.toggle_comment', times: 2, beforeDelay: 1000}
wait: 1000
moveTo: 2:11
wait: 1000
run: {command: 'emmet.toggle_comment', times: 2, beforeDelay: 1000}
</textarea>
