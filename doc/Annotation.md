# Information for Annotators

## Getting Started

Here is what you need to get started quickly.
For [more information on git and GitHub](#git-and-the-github-app), see below.

1. Create an account on [GitHub](https://github.com/).
   Let us know your username so that we can give you write access on this repository.
1. Install the [GitHub desktop app](https://desktop.github.com/) and log in with your account
   ([more information](#installing-the-github-app)).
1. "Clone" this repository.
   1. In the GitHub app, go to `File -> Clone repository`.
   1. Go to the tab `URL` and enter `https://github.com/DCMLab/schema_annotation_data.git`.
   1. Remember the `Local path` where the repository will be saved.
      You can also look that later up via `Repository -> Show in your File Manager`.
   1. Click on `Clone`.
1. Use the [annotation tool](https://dcmlab.github.io/schema_annotation_app/) to make your annotations.
   1. You'll find the input files (score, suggestions, etc.)
      in the directory to which you cloned this repository
      under `data/<corpus>/` (e.g. `data/mozart_sonatas/`).
   1. Make your annotations by following the instructions and the app and the [annotation manual](../manual/manual.pdf).
   1. **Double check your annotations!**
      The app currently does not check whether you entered a valid instance
      of the schema that you are annotating.
   1. Click on `Download Annotations` to download a file with your annotations.
      Put this file into `data/<corpus>/annotations/<schema>/`.
      If the `<schema>` directory does not exist,
      create it with the exact name of the schema variant.
1. Commit and push your changes.
   1. In the GitHub app, make sure that all changes that you want to commit
      are selected in the side bar.
   1. At the bottom of the side bar, write a short (one-line) summary of your changes.
      If you want, you can add a longer description in the box below.
   1. Click on `Commit to master`.
   1. Push your changes to GitHub by clicking on `Push origin` in the toolbar on the top.
   1. If you cannot push, someone else might have made changes in the meantime.
      Follow the suggestions of the GitHub app
      and use a combination of `Fetch`, `Pull`, and `Push` to merge these changes with yours.
      See below for [more information on git conflicts](#conflicts).

## Git and the GitHub App

In order to get the files you need for annotation and to upload the annotations you created,
we use git.
Git is a "version control system", i.e. it can track different versions of files,
such as the source code or data files.
All files belonging to a project are collected in a "repository".
Each new version of the repository is called a "commit".

TODO

### Installing the GitHub App

Download and install the GitHub Desktop App:

- **On Ubuntu:** In the terminal, run the command line
  ```
  $ sudo snap install github-desktop --beta --classic
  ```
- **On Windows:** 
  1. Visit the [GitHub Desktop App webpage](https://desktop.github.com/).
  1. Choose **Download for Windows**.
  1. Launch the downloaded file and click **Install**.
- **On MacOS:**
  1. Visit the [GitHub Desktop App webpage](https://desktop.github.com/).
  1. Choose **Download for Mac**.
  1. Unzip the downloaded file.
  1. *Optional:* Move **GitHub Desktop** to the **Applications** folder.

Start the app and log in with the account that has access to this repository.

### Using Git

TODO

### Conflicts
