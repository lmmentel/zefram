==============
zefram package
==============

A convenent, pythnonic way of interacting with data from the [IZA Database of Zeolite Structures](http://www.iza-structure.org/databases/).


Dependencies
============

* SQLAlchemy_
* numpy_

Installation
============

Simplest way to install ``zefram`` is with ``pip``:

.. code-block:: bash

   pip install zefram


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

Data
====

+--------------------------+-------+---------------------------------------------+-------------+
| Attribute                | Type  | Comment                                     | Data Source |
+==========================+=======+=============================================+=============+
| a                        | float | *a* unit cell length in Angstroms           | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| b                        | float | *b* unit cell length in Angstroms           | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| c                        | float | *c* unit cell legth in Angstroms            | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| alpha                    | float | *alpha* unit cell angle in degrees          | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| beta                     | float | *c* unit cell angle in degrees              | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| gamma                    | float | *c* unit cell angle in degrees              | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| code                     | str   | three letter framework code                 | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| name                     | str   | name of the framework in english            | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| atoms                    | int   | number of atoms in the unit cell            | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| portals                  | int   | number of portals in the unit cell          | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| cages                    | int   | number of cages in the unit cell            | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| channels                 | int   | number of channels in the unit cell         | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| junctions                | int   | number of junctions in the unit cell        | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| connections              | int   | number of connections in the unit cell      | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| tpv_abs                  | float | total pore volume in cm^3/g                 | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| tpv_rel                  | float | relative total pore volume in %             | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| lcd                      | float | largest cavity diameter in Angstrom         | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| pld                      | float | pore limiting diameter in Angstrom          | [2]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| accessible_area          | float | accessible area in Angstrom^2               | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| accessible_area_m2pg     | float | accessible area in m^2/g                    | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| accessible_volume        | float | accessible volume in Angstrom^3             | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| accessible_volume_pct    | float | accessible volume in %                      | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| channel_dim              | int   | channel dimensionality                      | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| cif                      | str   | cif file contents                           | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| framework_density        | float | number of T-atoms per 1000 Angstrom^3       | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| isinterrrupted           | bool  | interrrupted framework                      | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| isdisordered             | bool  | disordered framework                        | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| maxdsd_a                 | float | maximum diameter of a sphere that can       | [1]_        |
|                          |       | diffuse along *a*                           |             |
+--------------------------+-------+---------------------------------------------+-------------+
| maxdsd_b                 | float | maximum diameter of a sphere that can       | [1]_        |
|                          |       | diffuse along *b*                           |             |
+--------------------------+-------+---------------------------------------------+-------------+
| maxdsd_c                 | float | maximum diameter of a sphere that can       | [1]_        |
|                          |       | diffuse along *c*                           |             |
+--------------------------+-------+---------------------------------------------+-------------+
| maxdsi                   | float | maximum diameter of a sphere that can be    | [1]_        |
|                          |       | included                                    |             |
+--------------------------+-------+---------------------------------------------+-------------+
| occupiable_area          | float | occupiable area in Angstrom^2               | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| occupiable_area_m2pg     | float | occupiable area in m^2/g                    | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| occupiable_volume        | float | occupiable volume in Angstrom^3             | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| occupiable_volume_pct    | float | occupiable volume in %                      | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| specific_accessible_area | float | accessible area per unit volume in m^2/cm^3 | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| specific_occupiable_area | float | occupiable area per unit volume in m^2/cm^3 | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| td10                     | float | approximate topological density             | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| topological_density      | float | topological density                         | [1]_        |
+--------------------------+-------+---------------------------------------------+-------------+
| url_iza                  | str   | link to the source [1]_ for this framework  |             |
+--------------------------+-------+---------------------------------------------+-------------+
| url_zeomics              | str   | link to the source [2]_ for this framework  |             |
+--------------------------+-------+---------------------------------------------+-------------+

.. [1] `IZA database of zeolite structures <http://www.iza-structure.org/databases/>`_
.. [2] `ZEOMICS database <http://helios.princeton.edu/zeomics/>`_




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
