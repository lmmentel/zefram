==============
zefram package
==============


Dependencies
============

* SQLAlchemy_
* numpy_

Installation
============

After downloading and unpacking enter the ``zefram`` directory and install by

.. code-block:: bash

   python setup.py install [--user]


.. _SQLalchemy: http://www.sqlalchemy.org
.. _numpy: http://www.numpy.org

Usage
=====

The package exposes a simple API to access the database. ``framework`` method
acceps either three letter framework codes such as *AFI* or *MFI* or a list of
such strings returning a ``Framework`` object (or list of objects). The example
below shows also the accessible attributes of the ``Framework`` object

.. code-block:: python

    >>> from zefram import framework
    >>> afi = framework('AFI')
    >>> sorted(list(afi.__dict__.keys()))
    ['_sa_instance_state',
    '_spacegroup_id',
    'a',
    'accessible_area',
    'accessible_area_m2pg',
    'accessible_volume',
    'accessible_volume_pct',
    'alpha',
    'atoms',
    'b',
    'beta',
    'c',
    'cages',
    'channel_dim',
    'channels',
    'cif',
    'code',
    'connections',
    'framework_density',
    'gamma',
    'id',
    'isdisordered',
    'isinterrupted',
    'junctions',
    'lcd',
    'maxdsd_a',
    'maxdsd_b',
    'maxdsd_c',
    'maxdsi',
    'name',
    'occupiable_area',
    'occupiable_area_m2pg',
    'occupiable_volume',
    'occupiable_volume_pct',
    'pld',
    'portals',
    'rdls',
    'sbu',
    'specific_accessible_area',
    'specific_occupiable_area',
    'td10',
    'topological_density',
    'tpw_abs',
    'tpw_pct',
    'url_iza',
    'url_zeomics']


License
=======

| The MIT License (MIT)
| 
| Copyright (c) 2015 Lukasz Mentel
| 
| Permission is hereby granted, free of charge, to any person obtaining a copy
| of this software and associated documentation files (the "Software"), to deal
| in the Software without restriction, including without limitation the rights
| to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
| copies of the Software, and to permit persons to whom the Software is
| furnished to do so, subject to the following conditions:
| 
| The above copyright notice and this permission notice shall be included in all
| copies or substantial portions of the Software.
| 
| THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
| IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
| FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
| AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
| LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
| OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
| SOFTWARE.
