## Important

To convert Rmd to ipynb:

From Anaconda Prompt:

```
notedown --nomagic test.Rmd > test.ipynb
```

Then:

```
python rify.py test.ipynb
```

which will add the metadata so that the R kernel will start automatically in Binder.

[Source](https://github.com/jupyterhub/binderhub/issues/261#issuecomment-345987238)
