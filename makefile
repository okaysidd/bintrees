# Author:  mozman
# License: MIT-License

FLAGS = --inplace --force
CMD = setup.py build_ext
RUNTESTS = -m unittest discover

PYTHON27 = py -2.7
PYTHON35 = py -3.5
PYTHON36 = py -3.6
PYPY = C:\pypy2-5.6.0\pypy.exe

build27:
	$(PYTHON27)  $(CMD) $(FLAGS)

build35:
	$(PYTHON35) $(CMD) $(FLAGS)

build36:
	$(PYTHON36) $(CMD) $(FLAGS)

test27:
	$(PYTHON27) $(RUNTESTS)

test35:
	$(PYTHON35) $(RUNTESTS)

test36:
	$(PYTHON36) $(RUNTESTS)

testpypy:
	$(PYPY) $(RUNTESTS)

buildall: build27 build35 build36

testall: test27 test35 test36 testpypy

packages:
	$(PYTHON27) setup.py sdist --formats=zip
	$(PYTHON27) setup.py bdist_wheel
	$(PYTHON27) setup.py bdist --formats=wininst
	$(PYTHON35) setup.py bdist_wheel
	$(PYTHON35) setup.py bdist --formats=wininst
	$(PYTHON36) setup.py bdist_wheel
	$(PYTHON36) setup.py bdist --formats=wininst


release:
	$(PYTHON27) setup.py sdist --formats=zip upload
	$(PYTHON27) setup.py bdist_wheel upload
	$(PYTHON27) setup.py bdist --formats=wininst upload
	$(PYTHON35) setup.py bdist_wheel upload
	$(PYTHON35) setup.py bdist --formats=wininst upload
	$(PYTHON36) setup.py bdist_wheel upload
	$(PYTHON36) setup.py bdist --formats=wininst upload