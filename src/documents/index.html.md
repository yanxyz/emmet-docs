---
layout: default
title: Emmet 文档
---
# Emmet — 网页开发者必备工具

Emmet (previously known as _Zen Coding_) is a web-developer’s toolkit that can greatly improve your HTML & CSS workflow:

Emmet (即之前著名的 _Zen Coding_) 是一个网页开发者工具，可以大大地提高你的 HTML & CSS 开发效率。

<textarea class="movie-def">
&lt;!doctype html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;title&gt;Demo&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    |
&lt;/body&gt;
&lt;/html&gt;
~~~
tooltip: Type CSS-like abbreviation
type: ul#nav>li.item$*4>a{Item $}
wait: 1000
tooltip: Run “Expand Abbreviation” action to expand it into HTML ::: “Expand Abbreviation” (Tab key)
wait: 600
run: emmet.expand_abbreviation
wait: 1000
tooltip: Traverse between important code points with “Next/Previous Edit Point” action ::: “Next Edit Point” (Ctrl-Alt-→) <br> “Previous Edit Point” (Ctrl-Alt-←)
wait: 1000
run: {command: 'emmet.next_edit_point', times: 7}
wait: 1000
tooltip: Select tags with “Match Tag Pair” action ::: “Match Pair” (Cmd-D)
run: {command: 'emmet.match_pair_outward', times: 3}
wait: 1000
moveTo: 102
tooltip: Select important parts with “Select Next/Previous Item” action ::: “Select Next Item” (Shift-Cmd-.) <br> “Select Previous Item” (Shift-Cmd-,)
run: {command: 'emmet.select_next_item', times: 7, beforeDelay: 300}
wait: 2000
moveTo: 95
wait: 1000
tooltip: Quickly comment full tag with “Toggle Comment” action ::: “Toggle Comment” (Cmd-/)
run: {command: 'emmet.toggle_comment', times: 2, beforeDelay: 1000}
</textarea>

Basically, most text editors out there allow you to store and re-use commonly used code chunks, called _“snippets”_. While snippets are a good way to boost your productivity, all implementations have common pitfalls: you have to define the snippet first and you can’t extend them in runtime.

基本上当下大多数文本编辑器可以重用常用的代码块，称为“代码片断”（ _snippets_ ）。代码片断是提高生产效率的好办法，不过所有的实现都有共同的缺陷：要先定义代码片断并且不能实时展开。

Emmet takes the snippets idea to a whole new level: you can type _CSS-like_ expressions that can be dynamically parsed, and produce output depending on what you type in the abbreviation. Emmet is developed and optimised for web-developers whose workflow depends on HTML/XML and CSS, but can be used with programming languages too.

Emmet 将代码片断的思想提升到全新的高度：书写类似于 CSS 的表达式，然后实时解析展开。Emmet 是为了HTML/XML 与 CSS 而开发，也最适合用于它们，不过也能与编程语言一块使用。

Start learning Emmet with the [abbreviation syntax](/abbreviations/) and available [actions](/actions/).

开始学习 Emmet： [缩写](/abbreviations/) 与 [功能](/actions/)。

<a href="http://emmet.io/download/" class="btn btn-primary download-main">Download<span class="download-main__comment">plugin for your favourite editor</span></a>

译注：官方没有开发 Vim 插件，需要的请查看[emmet-vim](http://www.zfanw.com/blog/zencoding-vim-tutorial-chinese.html)。
