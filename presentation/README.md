# LaTeX Beamer Theme

This repository contains the (unofficial) LaTeX version of the new FAU template for presentations at
the Faculty of Engineering. In addition, it also contains the `i2beamer` package that builds upon
the template and that defines additional commands, environments, and styles.

## The 'fau' Beamer Theme

The `fau` beamer theme can be found in the subdirectory `_template/beamerthemefau/`. To use this
theme, simply use the standard `\usetheme` command in your document's preamble (this requires that
the subdirectory that contains the theme is included in the `TEXINPUTS` search path):

    \usetheme{fau}

**Note**: Using the `fau` beamer theme requires *two* consecutive runs of `pdflatex` to build the
slides correctly.

The `fau` theme supports the following options:

- `wide`: If this option is set, the slides use a 16:9 aspect ratio (instead of the default 4:3
  aspect ratio).
- `lettering=<file path>`: By default, the FAU logo on the title page is accompanied by the
  lettering "Friedrich-Alexander-Universität Erlangen-Nürnberg" (which is included as a graphic).
  This lettering can be replaced by setting the `lettering` option and by providing the path to a
  different graphics file as argument. For example, the `i2beamer` package sets this option to
  display the lettering "Friedrich-Alexander-Universität Programming Systems Group" instead.
- `logolarge=<file path>`: If this option is set, the graphics file provided as an argument is
  included as additional logo on the title page (in this case, the FAU logo is moved from the right
  hand side of the slide to the left). For example, the `i2beamer` package sets this option to
  include the logo of the Programming Systems Group.
- `logosmall=<file path>`: If this option is set, the graphics file provided as an argument is
  included as a (very small) logo in the footer of each slide. For example, the `i2beamer` package
  sets this option to include the logo of the Programming Systems Group.
- `plain`: If this option is set, the title page does not include the background image (blue waves),
  but uses a plain, solid background instead.

## The 'i2beamer' Package

The `i2beamer` package builds upon the `fau` beamer theme and defines additional commands,
environments, and styles. It can be found in the subdirectory `_template/i2beamer/`. To include this
package, simply use the standard `\usepackage` command in your document's preamble (this requires
that the subdirectory that contains the package is included in the `TEXINPUTS` search path):

    \usepackage{i2beamer}

**Note**: The `i2beamer` package already includes the `fau` beamer theme for you (i.e., you should
omit the `\usetheme` command when using the `i2beamer` package).

The `i2beamer` package supports the following options:

- `wide`: If this option is set, the slides use a 16:9 aspect ratio (instead of the default 4:3
  aspect ratio).
- `english`: If this option is set, some language-specific things are set to english.
- `logo`: If this option is set, the slides contain the logo of the Programming Systems Group on the
  title page and in the footer of each slide.
- `plain`: If this option is set, the title page does not include the background image (blue waves),
  but uses a plain, solid background instead.

## Example Presentation

This repository also contains an example presentation that uses the `fau` theme and the `i2beamer`
package (`talk.tex` in the root directory). It not only serves as an example for the theme, but also
demonstrates how to use the additional features that the `i2beamer` package provides. It is
accompanied by the `Makefile` that shows how to correctly build the presentation (a simple `make`
should suffice).
