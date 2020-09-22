# Additional HonKit module

## Math

The source page mentioned that you can use MathJax or Katex to add math rendering capability to HonKit. But I am having issue on MathJax installation. It could be versioning problem of `npm`. Now I use Katex and it works.

To install Katex for HonKit, do:

```
D:\storage\honkit> npm install Katex
D:\storage\honkit> npm install gitbook-plugin-Katex
D:\storage\honkit> npm list -depth=0
docs@1.0.0 D:\STORAGE\honkit
+-- gitbook-plugin-katex@1.1.4
+-- honkit@3.6.6
`-- katex@0.12.0
```

and write math fenced with \$\$ sign. Example:  

$$
F=ma
$$
