# pablodecm.com

This is the code to generate the current version of my personal webpage (<https://pablodecm.com>)
that will be improved in the future.

## Environment

The following instructions have only been tested with with MacOS and python3.9.
It is recommended to create a virtual environment.

First we need to use Git to clone this repository, ideally using the recursive
flag to also include the theme:

```bash
git clone --recursive git@github.com:pablodecm/pablodecm.com.git
```

We can the access the project and create a virtual environment:

```bash
cd pablodecm.com
python3.9 -m venv pelican_env
source pelican_env/bin/activate
pip install -r requirements.txt
```

We should now have all key software dependencies but we also need to bring the
pelican plugins to this folder:

```bash
git clone --recursive git@github.com:getpelican/pelican-plugins.git
```

We can the simply use either [standard pelican commands](https://docs.getpelican.com/en/latest/quickstart.html)
or those in the Makefile to do the different operations:

```bash
make html # creates html output
make serve # serves output
make devserve # serves output in auto-reload mode
```
