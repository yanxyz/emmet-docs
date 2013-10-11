---
layout: page
title: 厂商前缀
menuOrder: 1
---
New CSS3 features are a blessing for web-developers: with a few lines of code we can do things that were nearly impossible a few years ago. But these features are also a real pain for us: we have to write the same property many times for different browsers.

新的 CSS3 特性是开发者的福音：几行代码可以做到几年前几乎做不到的事。但是同时也给我们带来一个痛苦：一个属性需要为不同的浏览器重复写几遍。

Emmet’s CSS resolver has a nice feature that can greatly improve your CSS3 experience. Every time you precede CSS property or its abbreviation with a hyphen, Emmet automatically creates vendor-prefixed copies of this property. For example, `-bdrs` abbreviation will be expanded into

Emmet 的 CSS 解析器提供一个不错的功能，可以大大提高你的 CSS3 开发体验。在属性前或缩写前放一个连字符，Emmet 会自动给这个属性添加厂商前缀。例如缩写 `-bdrs` 将展开为：

```css
-webkit-border-radius: ;
-moz-border-radius: ;
border-radius: ;
```

Moreover, in editors with tabstops support (such as Eclipse, Sublime Text 2, Espresso etc.) Emmet will create a linked value placeholder so you can type a property value and it will be automatically placed in all generated properties.

而且对于支持插入占位的编辑器（Eclipse, Sublime Text 2, Espresso 等），Emmet 将创建关联的属性值占位，输入一次将自动插入到所有生成的属性中。

## How it works? 工作原理

Whenever you expand abbreviation with a hyphen in front of it, Emmet removes the hyphen and looks for a snippet definition in `snippets.json` for the rest of the abbreviation. For example, for `-bdrs` abbreviation it will look for a `bdrs` definition. `snippet.json` has the following definition:

缩写前放一个连字符，展开时，Emmet 移除连字符，然后在 `snippets.json` 里查找缩写的定义。例如 `-bdrs` 将查找 `bdrs`：

	"bdrs": "border-radius:|;"

...which means that `bdrs` will be expanded into `border-radius` property. If no definition found, the abbreviation itself will be used as a CSS property name.

`bdrs` 将展开为 `border-radius` 属性。如果没有找到定义，缩写将用作一个属性名。

After the CSS resolver figures out a property name that should be outputted, it will look for its occurrence in special _vendor catalogs_. These catalogs are defined as `css.{vendor}Properties` entries in preferences and can be overridden by user. `{vendor}` is a browser’s vendor prefix, for example, `webkit`, `moz` etc.

当 CSS 解析器知道要输出属性名后，便在“厂商分类”中查找此属性名。这些分类在配置里由 `css.{vendor}Properties` 定义。`{vendor}` 是浏览器厂商前缀，比如 `webkit`, `moz` 等。

If the expanded property was found in any of these catalogs, their vendor prefixes will be used to produce prefixed properties. Otherwise, _all prefixes_ will be used.

如果在厂商分类中找到了，这些厂商前缀将用于生成带前缀的属性。如果没找到则使用所有的前缀。

For example, the `border-radius` property is defined in `css.webkitProperties` and `css.mozProperties` so this property will be outputted with `webkit` and `moz` prefixes. On the other hand, a `foo` property isn’t defined anywhere so it will be outputted with all available prefixes when you expand `-foo` abbreviation: `webkit`, `moz`, `ms` and `o`. It is especially helpful for using cutting-edge CSS properties that were recently implemented.

例如属性`border-radius` 在 `css.webkitProperties` 和 `css.mozProperties` 中有定义，这个属性输出时将带上前缀 `webkit` 和 `moz`。属性 `foo` 在所有分类中均没有定义，则展开缩写 `-foo` 时将带上所有前缀: `webkit`, `moz`, `ms` and `o`。这个功能在使用刚实现的 CSS 属性时特别有用。

Imagine that Google Chrome implemented `super-foo` property yesterday and you want to use it in your project. You can expand `-super-foo` abbreviation which results in the following snippet:

假定昨天 Google Chrome 实现了属性 `super-foo`，你打算用在项目中，展开 `-super-foo` 得到：

```css
-webkit-super-foo: ;
-moz-super-foo: ;
-ms-super-foo: ;
-o-super-foo: ;
super-foo: ;
```

## Add prefixed properties by default 默认添加厂商前缀

While writing CSS files, you may find that a “clear” CSS3 property is useless without its vendor-prefixed variants.  It makes writing hyphenated abbreviations like `-trf` (`trf` is an alias to `transform` property) a bit awkward.

一个 CSS3 属性如果没有厂商前缀可能就没用，这样书写带连字符的缩写不方便。

This is why Emmet has `css.autoInsertVendorPrefixes` preference enabled by default. With this preference enabled, all CSS properties defined in vendor catalogs will be automatically supplied with matched vendor-prefixed variants.

这便是 Emmet 为什么默认启用选项 `css.autoInsertVendorPrefixes`。当启用这个选项后，所有在厂商分类里定义的 CSS 属性将自动添加相应的厂商前缀。

It means that you don’t need to use a hyphen to get valid prefixed variants for known CSS properties, simply expand abbreviations like `bdrs` or `trf` to get a valid list of vendor-prefixed properties.

这意味着不需要对已定义的 CSS 属性使用连字符去添加厂商前缀。例如展开 `bdrs` 或 `trf`，将得到一列带有厂商前缀的属性。

## Explicit vendor prefixed 显式添加厂商前缀

Sometimes you may want to output CSS properties with specified vendor prefixed properties only.

有时你只想输出指定厂商前缀的 CSS 属性。

Let’s say you want to output `transform` property with `webkit` and `moz` prefixes only. In this case you can expand the following abbreviation:

比如说输出属性 `transform`，只带有前缀 `webkit` 与 `moz`。在这种情况下展开下面缩写：

	-wm-trf

As you can see, we slightly modified the abbreviation by adding a list of one-letter prefixes. In this case, these are `w` (`webkit`) and `m` (`moz`) prefixes. Emmet has the following one-letter prefixes:

如你所见，添加单字符的前缀列表可以修改缩写。这个例子中是 `w` (`webkit`) 和 `m` (`moz`)。Emmet 支持下面单字符前缀：

* `w`: `webkit`
* `m`: `moz`
* `s`: `ms`
* `o`: `o`

译注：目前的趋势是浏览器在实现新属性时不再使用厂商前缀，而是通过特性开关来启用。这样可以避免厂商前缀带来混乱。