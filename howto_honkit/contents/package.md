# Additional HonKit module

## Math

The source page mentioned that you can use MathJax or Katex to add math rendering capability to HonKit. I had issues on MathJax installation and turned out it was versioning problem of the dependencies.

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

Installing MathJax uses `gitbook-plugin-mathjax`. But the version of the packages must be correct.

```
D:\storage\honkit> npm list -depth=0
docs@1.0.0 D:\STORAGE\honkit
+-- gitbook-plugin-mathjax@1.1.2
+-- honkit@3.6.6
`-- mathjax@2.7.9
```

To install a package with specific version use:

```
npm install mathjax@2.7.9
```
