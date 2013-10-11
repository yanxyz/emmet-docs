---
layout: page
title: "编码/解码图像为 data:URL"
menuOrder: 14
---
HTML and CSS allows you to embed external resources right into base using [data:URL](http://en.wikipedia.org/wiki/Data_URI_scheme) scheme. Usually, image conversion to base64 is done with external on-line services or third-party assets builder. 

HTML 与 CSS 可以用 [data:URL](http://en.wikipedia.org/wiki/Data_URI_scheme) 插入外部资源。通常用在线服务或第三方软件将图像转换为 base64。

But these tools have downsides: you have to spend extra time on on-line tools or loose control on images that should or should not be converted to base64.

但是这些工具有缺点：在线工具要花费额外的时间，或者不能控制图片是否应该转换为 base64。

With Emmet, you can convert image to data:URL right in your editor, as well as convert it _back to external file_.

使用 Emmet 在编辑器里就可以将图像转换为 base64，或者相反操作。

<textarea class="movie-def">
body {
    background: url(demo.png);
}
@@@
tooltip: Move caret inside image path
wait: 1000
moveTo: 1:24
wait: 1000
tooltip: Run “Encode/Decode Image to data:URL” action ::: “Encode/Decode Image to data:URL” (Shift-Cmd-I)
run: emmet.encode_decode_data_url
@@@
mode: text/css
</textarea>