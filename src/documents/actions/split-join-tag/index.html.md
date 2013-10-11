---
layout: page
title: 分割合并标签
menuOrder: 7
---
This action splits and joins tag definition, e.g. converts from `<tag/>` to `<tag></tag>` and vice versa. Very useful for XML/XSL developers.

这个功能分割合并标签，例如将`<tag/>` 转换为 `<tag></tag>` ，或逆操作。对于 XML/XSL 开发很有用。

<textarea class="movie-def">
&lt;example&gt;
	|Lorem ipsum dolor sit amet
&lt;/example&gt;
~~~
run: emmet.split_join_tag ::: “Split/Join Tag” (Cmd-J)
wait: 1000
moveTo: 6
wait: 1000
run: emmet.split_join_tag
</textarea>

----------------

“Split/Join Tag” action uses “[HTML Matcher](/actions/match-pair/)” internally so it may work in non-HTML syntaxes too.

这个功能在内部调用 [匹配标签](/actions/match-pair/) 功能，所以非 HTML 语法也可以用。
