---
layout: page
title: 更新图片尺寸
menuOrder: 10
---
Many web-developers forget to write _width_ and _height_ attributes  for `<img>` tags which leads to poor UX. This action helps you to automate this process: simply place caret inside `<img>` tag and run this action to add/update width and height attributes.

许多开发者忘记给 `<img>` 标签添加 _width_ 与 _height_ 属性，这样对用户体验不好。这个功能自动帮你搞定：将插入符放在 `<img>` 标签内，然后调用此功能，就可以添加或更新 width 与 height 属性。

In CSS, place caret inside property value with `url()` function to add/update width and height properties for current rule.

对于 CSS，将插入符放在属性值 `url()` 内，然后调用此功能，就可以添加或更新 width 与 height 属性。

<textarea class="movie-def">
|&lt;img src="demo.jpg" alt="" /&gt;
&lt;style&gt;
.block {
	background: url(demo.jpg);
}
&lt;/style&gt;
~~~
tooltip: Put caret inside &lt;img&gt; tag and run “Update Image Size” to get its size
moveTo: 6
wait: 1000
run: emmet.update_image_size ::: “Update Image Size” (Shift-Cmd-U)
wait: 1000
tooltip: Put caret inside value with image URL to update width and height properties of the rule
moveTo: 3:22
wait: 1000
run: emmet.update_image_size
</textarea>

Note that this action also works for absolute URLs: it will start searching for requested file from host file’s folder and then will traverse up the tree.

注意此功能对绝对 URL 路径也适用：从宿主文件所在目录开始查找文件，然后沿着目录结构向上查找。