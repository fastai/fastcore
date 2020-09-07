.ONESHELL:
SHELL := /bin/bash
SHELLFLAGS := -e

SRC = $(wildcard nbs/*.ipynb)

all: fastcore docs

fastcore: $(SRC)
	nbdev_build_lib
	touch fastcore

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	rsync -a docs_src/ docs
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi tag
	sleep 10
	nbdev_conda_package --upload_user fastai --build_args '-c pytorch -c fastai'
	nbdev_bump_version

conda_release:
	nbdev_conda_package --upload_user fastai --build_args '-c pytorch -c fastai'

tag:
	export TAG="$$(python setup.py version)"
	echo "$$(python setup.py version)"
	echo "$${TAG}"
	git tag "$${TAG}"
	git push --tags
	gh api repos/:owner/:repo/releases -F tag_name="$${TAG}" -F name="$${TAG}"

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist

