# Internal Documentation

## Repository Structure

### Data Files: `data/`

- `lexicon.json`: the schema lexicon

Each sub-corpus is stored in a self-contained directory, e.g. `mozart_sonatas`.
Within each of these directories (called `<dir>/` below) the same substructure is used:

- `<dir>/mscore`: contains musescore source files
- `<dir>/musicxml`: contains prepared musicxml files,
  generated from the sources and augmented with note IDs
- `<dir>/notelist/` contains the representation of each piece as a JSON note list.
- `<dir>/annotations`: contains schema annotations
  - `<dir>/annotations/<schema>`: contains the annotations for a specific schema template,
    e.g. `<dir>/schemata/fonte.2` for the `fonte.2` schema template.
- `<dir>/groups/`:
  - `<dir>/groups/<schema>` contains the suggestions for a schema in JSON.

### Conversion Tools `tools/`

Contains tools for data preparation, post-processing, etc. (see below).

### Documentation `doc/`

Contains the documentation for annotators, developers, and curators.

### Annotation Manual `manual/`

Contains the annotation manual, including LaTeX sources.

## Preparation of the Data

For every corpus, follow these steps:

1. Make sure that the encoding is correct and unambiguous.
   In particular, take care of repetitions.
2. Convert the MuseScore sources (`data/<dir>/mscore`) to MusicXML (`data/<dir>/musicxml`).
3. Add note IDs to the MusicXML files in `data/<dir>/musicxml`.
4. Generate note lists (tbd.)
5. Precompute suggestions (tbd.)

Steps 2 and 3 can be performed by running `mscx_to_xml.sh` from the `tools/` directory.
In order for this to work, you first need to setup a virtual environment in the `tools/` directory
and install some python dependencies.
This is done automatically by the `setup.sh` script.
You only need to run this script once.

``` shell
$ cd tools
$ ./setup.sh # only do this the first time
$ ./mscx_to_xml ../data/<dir>/mscore ../data/<dir>/musicxml
```

This is currently very slow, because it compiles every file every time.
In the future, this functionality will be moved to a makefile.

Steps 4 and 5 still need to be documented.
