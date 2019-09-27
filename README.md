# Schema Annotation Data

Contains the source and annotation data for the schema annotation project.

## Repository Structure

Each sub-corpus is stored in a self-contained directory, e.g. `mozart_sonatas`.
Within each of these directories (called `dir/` below) the same substructure is used:

- `dir/mscore`: contains musescore source files
- `dir/musicxml`: contains prepared musicxml files,
  generated from the sources and augmented with note IDs
- `dir/schemata`: contains schema annotations
  - `dir/schemata/<schema>`: contains the annotations for a specific schema template,
    e.g. `dir/schemata/fonte.2` for the `fonte.2` schema template.

### General Files

- `lexicon.json`: the schema lexicon
- `Makefile`: automates data preparation using `make` (coming soon)
- `tools/`: contains tools for data preparation, post-processing, etc.

## Preparation of the Data

1. Make sure that the encoding is correct and unambiguous.
   In particular, take care of repetitions.
2. Convert the MuseScore sources (`dir/mscore`) to MusicXML (`dir/musicxml`).
3. Add note IDs to the MusicXML files in `dir/musicxml`.

Steps 2 and 3 can be performed by running `mscx_to_xml.sh` from the `tools` directory.
In order for this to work, you first need to setup a virtual environment in the `tools` directory
and install some python dependencies.
This is done automatically by the `setup.sh` script.
You only need to run this script once.

``` shell
$ cd tools
$ ./setup.sh # only do this the first time
$ ./mscx_to_xml ../dir/mscore ../dir/musicxml
```

This is currently very slow, because it compiles every file every time.
In the future, this functionality will be moved to a makefile.
