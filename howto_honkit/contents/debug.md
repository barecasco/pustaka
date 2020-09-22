# Bugs Found

##### Lunr Search Doesn't Work

The search function only works upon HonKit first run (`serve`/`build`). After that, it returns nothing. No solution has been found from internet or local effort.

The search bar and the backend engine `lunr` are disabled in `book.json`.

```
{
    "plugins": [
        "-lunr",
        "-search"
    ]
}
```

##### `split` Method of undefined on GLOSSARY Page

When clicking a GLOSSARY word, an error of accesing `split` method of `undefined` is thrown. The page works normal, so I just normalize the responsible function at:

`node_modules\@honkit\honkit-plugin-theme-default\_assets\website\theme.js`

by only returning the eventual value no matter what happened upon call:

```
function c(e){var t=e.children("a"),n="";return "";}
```

Therefore no error notification is raised.  
