#! /usr/bin/make
.PHONY: default local_serve copy_assets
ASSETS:= diagram.svg

default: copy_assets

local_serve: 
	bundle exec jekyll serve

# must be done after the jekyll exec
copy_assets: $(ASSETS)
	cp $^ docs/_site/assets/.
