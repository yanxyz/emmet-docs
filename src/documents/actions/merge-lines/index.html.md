---
layout: page
title: 合并行
menuOrder: 9
---
Many editors have similar action: it merges selected lines into a single one. But when there’s no selection, Emmet will match context HTML tag.

许多编辑器有类似功能：将选中的多行合并为单行。不过如果没有选择，Emmet 将匹配所在 HTML 标签。

<textarea class="movie-def">
&lt;p&gt;
	Lorem ipsum dolor sit amet.
	|Officiis animi consequuntur iure.
	Ea asperiores aperiam non necessitatibus?
	Expedita iusto cupiditate eum esse
&lt;/p&gt;
~~~
run: emmet.merge_lines ::: “Merge Lines” (Shift-Cmd-M)
</textarea>
