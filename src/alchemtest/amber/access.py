"""Accessors for Amber TI datasets.

"""

from os.path import dirname, join
from os import listdir
from glob import glob

from .. import Bunch



def load_bace_improper():
    """Load Amber Bace improper solvated vdw example

    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files for improper solvated vdw alchemical leg

    """
    module_path = dirname(__file__)
    data = {'vdw': glob(join(module_path, 'bace_improper/solvated/vdw/*/ti-*.out.bz2'))}

    with open(join(module_path, 'bace_improper', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)


def load_bace_example():
    """Load Amber Bace example perturbation.

    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by system and alchemical leg

    """
    module_path = dirname(__file__)
    data = {'complex':
                {'decharge': glob(join(module_path, 'bace_CAT-13d~CAT-17a/complex/decharge/*/ti-*.out.bz2')),
                 'recharge': glob(join(module_path, 'bace_CAT-13d~CAT-17a/complex/recharge/*/ti-*.out.bz2')),
                 'vdw': glob(join(module_path, 'bace_CAT-13d~CAT-17a/complex/vdw/*/ti-*.out.bz2'))
                 },
            'solvated':
                {'decharge': glob(join(module_path, 'bace_CAT-13d~CAT-17a/solvated/decharge/*/ti-*.out.bz2')),
                 'recharge': glob(join(module_path, 'bace_CAT-13d~CAT-17a/solvated/recharge/*/ti-*.out.bz2')),
                 'vdw': glob(join(module_path, 'bace_CAT-13d~CAT-17a/solvated/vdw/*/ti-*.out.bz2'))
                 }
            }

    with open(join(module_path, 'bace_CAT-13d~CAT-17a', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)


def load_simplesolvated():
    """Load the Amber solvated dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)
    data = {'charge': glob(join(module_path, 'simplesolvated/charge/*/ti-*.tar.bz2')),
            'vdw': glob(join(module_path, 'simplesolvated/vdw/*/ti-*.tar.bz2'))}

    with open(join(module_path, 'simplesolvated', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)


def load_invalidfiles():
    """Load the invalid files.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the example of invalid data files
        - 'DESCR': the full description of the dataset


    .. deprecated:: 0.7
        substituted by laod_testfiles

    """

    module_path = dirname(__file__)
    data = [glob(join(module_path, 'invalidfiles/*.out.bz2'))]

    with open(join(module_path, 'invalidfiles', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)


def load_testfiles():
    """Load incomplete-wrongly formatted files to be used to test the AMBER parsers.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files
        - 'DESCR': the full description of all the files

    """

    module_path = dirname(__file__)

    data = {}
    for f in listdir(join(module_path, 'testfiles')):
        if f.endswith('bz2'):
            data[f.strip(".out.tar.bz2")] = [join(module_path, 'testfiles', f)]

    with open(join(module_path, 'testfiles', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
