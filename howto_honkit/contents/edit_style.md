# Editing Style ala Agra

#### Font Families
We need to change 3 font families. Two fonts used for serif and sans, one font used for code. To change the serif and sans, set below parameter at file:

`node_modules\gitbook-plugin-fontsettings\assets\website.css`

```
...
.book.font-size-2 .book-body .page-inner section {
  font-size: 1.8rem;
  max-width:72rem;
}
.book.font-size-3 .book-body .page-inner section {
  font-size: 2.1rem;
}
...
.book.font-family-0 {
  font-family: Lora, Georgia, serif;
}
.book.font-family-1 {
  font-family: "Raleway", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

To change font for the code, go to:

`node_modules\gitbook-plugin-fontsettings\assets\website.css`

and find the line that contains `markdown-section pre{font-family:` and `Menlo`. Add new font "Roboto Mono" at the front of the list:

```
.markdown-section pre{font-family:"Roboto Mono",...;line-height:2rem;}
```

oh, and add the line-height parameter too, use 2rem so the code lines are not separated too far.

To make the fonts available for other users, currently we are finding a way to add google fonts to the index.html file at _book. The line that should be added is:

```
<link rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Lora&family=Raleway&family=Roboto+Mono">
```

#### Blend in any Hyperlink

Make any hyperlink invisible by blending in with body text color. Copy the color at White mode and Night mode and apply it to the hyperlink color. Open the file:

`node_modules\gitbook-plugin-fontsettings\assets\website.css`

```
...
.book.color-theme-2 .book-body .page-wrapper .page-inner section.normal {
  color: #bdcadb;
}
.book.color-theme-2 .book-body .page-wrapper .page-inner section.normal a {
  color: #bdcadb;
}
...
.book.color-theme-1 .book-body .page-wrapper .page-inner section.normal {
  color: #704214;
}
.book.color-theme-1 .book-body .page-wrapper .page-inner section.normal a {
  color: #704214;
}
```

Next, erase the underline of a link. Check inside file:

`node_modules\@honkit\honkit-plugin-theme-default\_assets\website\style.css`

and find any anchor -`a{`- that leads to setting up `text-decoration:underline` attribute. Erase that attribute.
