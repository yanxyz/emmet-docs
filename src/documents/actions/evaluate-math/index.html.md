---
layout: page
title: 计算数学表达式
menuOrder: 11
---
Evaluates simple math expression like `2*4` or `10/2` and outputs its result. You can use `\` operator which is equivalent to `round(a/b)`.

计算简单的数学表达式，比如`2*4` 或 `10/2`，并输出结果。`\` 操作符结果同 `round(a/b)`。

Very useful in CSS where numeric values should be modified frequently.

当数字值频繁改变时这个比较很有用。

<textarea class="movie-def">
|
~~~
tooltip: Enter simple math expression and run “Evaluate Math Expression” action
type: 2\*6
wait: 1000
run: emmet.evaluate_math_expression ::: “Evaluate Math Expression” (Shift-Cmd-Y)
wait: 1000
type: {text: ' 10\\\\3'}
wait: 1000
run: emmet.evaluate_math_expression
wait: 1000
type: {text: ' 20\*4+10'}
wait: 1000
run: emmet.evaluate_math_expression
</textarea>