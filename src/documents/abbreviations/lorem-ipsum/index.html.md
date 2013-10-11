---
layout: page
title: “Lorem Ipsum” 生成器
menuOrder: 4
---
[“Lorem ipsum”](http://www.lipsum.com) dummy text is used by many web-developers to test how their HTML templates will look with real data. Often, developers use third-party services to generate “Lorem ipsum” text, but now you can do that right in your editor. Just expand `lorem` or `lipsum` abbreviations to get the following snippet:

[“Lorem ipsum”](http://www.lipsum.com) 假文，许多开发者用它来测试 HTML 模板填充数据后的样子。开发者常常用第三方服务来生成假文，不过现在在编辑器里就能做到，只用展开 `lorem` 或 `lipsum` ：

	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi non quis exercitationem culpa nesciunt nihil aut nostrum explicabo reprehenderit optio amet ab temporibus asperiores quasi cupiditate. Voluptatum ducimus voluptates voluptas?

`lorem` is not just a normal snippet—it’s actually a _generator_. Every time you expand it, it will generate a 30-words dummy text, splitted into a few sentences.

`lorem` 不是普通的代码片断——它是一个 **生成器**。每次展开将生成 30 字数的假文，分为几个句子。

You can specify how many words should be generated right in the abbreviation. For example, `lorem100` will generate a 100-words dummy text.

可以指定字数。比如 `lorem100` 将生成 100 字数的假文。

## Repeated “Lorem ipsum”重复假文

You can use `lorem` generator inside repeated elements to create tags filled with completely random sentences. For example, `p*4>lorem` abbreviation would generate something like this:

在重复元素内使用 `lorem` 填充随机文本。比如 `p*4>lorem`：

	<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui dicta minus molestiae vel beatae natus eveniet ratione temporibus aperiam harum alias officiis assumenda officia quibusdam deleniti eos cupiditate dolore doloribus!</p>
	<p>Ad dolore dignissimos asperiores dicta facere optio quod commodi nam tempore recusandae. Rerum sed nulla eum vero expedita ex delectus voluptates rem at neque quos facere sequi unde optio aliquam!</p>
	<p>Tenetur quod quidem in voluptatem corporis dolorum dicta sit pariatur porro quaerat autem ipsam odit quam beatae tempora quibusdam illum! Modi velit odio nam nulla unde amet odit pariatur at!</p>
	<p>Consequatur rerum amet fuga expedita sunt et tempora saepe? Iusto nihil explicabo perferendis quos provident delectus ducimus necessitatibus reiciendis optio tempora unde earum doloremque commodi laudantium ad nulla vel odio?</p>

Also, `lorem` generator utilizes the [implicit tag name resolver](/abbreviations/implicit-names/) when `lorem` element is self-repeated so you can shorten your abbreviations:

`lorem` 也能 [解析隐式标签名](/abbreviations/implicit-names/)。当只重复 `lorem` 时可以简化缩写：

`ul.generic-list>lorem10.item*4`

...will produce

	<ul class="generic-list">
		<li class="item">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nam vero.</li>
		<li class="item">Laboriosam quaerat sapiente minima nam minus similique illum architecto et!</li>
		<li class="item">Incidunt vitae quae facere ducimus nostrum aliquid dolorum veritatis dicta!</li>
		<li class="item">Tenetur laborum quod cum excepturi recusandae porro sint quas soluta!</li>
	</ul>

