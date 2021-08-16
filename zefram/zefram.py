""" zefram module """

from __future__ import print_function

import argparse
import numpy as np
import pandas as pd
import os

from sqlalchemy import (
    Column,
    Table,
    Boolean,
    Integer,
    String,
    Float,
    create_engine,
    ForeignKey,
)
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property


def framework(codes):

    if isinstance(codes, (list, tuple)):
        return [get_framework(code) for code in codes]
    elif isinstance(codes, str):
        if len(codes) == 3:
            return get_framework(codes)
        else:
            raise ValueError("wrong framework code: {}".format(codes))
    else:
        raise ValueError(
            "Expected a <list>, <tuple> or <str> of length 3, got: {}".format(
                type(codes)
            )
        )


def get_framework(code):
    '''Return a database entry for framework matching the "code"'''

    session = get_session()

    return session.query(Framework).filter(Framework.code == code).one()


def get_session():
    """Return the database session connection."""

    dbpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "frameworks.db")
    engine = create_engine("sqlite:///{path:s}".format(path=dbpath), echo=False)
    db_session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return db_session()


def get_engine():
    """Return the database engine."""

    dbpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "frameworks.db")
    engine = create_engine("sqlite:///{path:s}".format(path=dbpath), echo=False)
    return engine


def get_table(tablename, **kwargs):
    """
    Return a table from the database as pandas DataFrame

    Args:
      tablename: str
        Name of the table from the database
      kwargs:
        A dictionary of keyword arguments to pass to the `pandas.read_qsl`

    Returns:
      df: pandas.DataFrame
        Pandas DataFrame with the contents of the table
    """

    tables = ["frameworks"]

    if tablename in tables:
        engine = get_engine()
        df = pd.read_sql(tablename, engine, **kwargs)
        return df
    else:
        raise ValueError("Table should be one of: {}".format(", ".join(tables)))


Base = declarative_base()


fw_rings = Table(
    "fw_rings",
    Base.metadata,
    Column("framework_id", Integer, ForeignKey("frameworks.id")),
    Column("ringsize_id", Integer, ForeignKey("ringsizes.id")),
)


fw_tilings = Table(
    "fw_tilings",
    Base.metadata,
    Column("framework_id", Integer, ForeignKey("frameworks.id")),
    Column("tiling_id", Integer, ForeignKey("naturaltilings.id")),
)


class RingSize(Base):
    """
    Framework ring sizes

    Attributes
      size : int
        Number of T atoms forming the ring
    """

    __tablename__ = "ringsizes"

    id = Column(Integer, primary_key=True)
    size = Column(Integer, nullable=False)

    def __repr__(self):
        return "<RingSizes(size={0:3d})>".format(self.size)


class NaturalTiling(Base):
    """
    Framework natural tiling

    Attributes
      name : str
        Name of the tiling, http://izasc.fos.su.se/fmi/xsl/IZA-SC/TilingList.htm
    """

    __tablename__ = "naturaltilings"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return "<NaturalTiling(name={0:s})>".format(self.name)


class SpaceGroup(Base):
    """
    Space Group

    Attributes:
      name : str
        Name of the space group
      number : int
        Space group integer label according to International Tables for
        Crystallography Volume A: Space-group symmetry,
        URL:http://it.iucr.org/A/
      cell_setting : str
        Additional cell settings
      cs_code : str
        Coordinate system code
    """

    __tablename__ = "spacegroups"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)
    cell_setting = Column(String)
    cs_code = Column(Integer)

    def __repr__(self):
        return (
            "<SpaceGroup(name={0}, number={1}, cell_setting={2}, cs_code={3}>".format(
                self.name, self.number, self.cell_setting, self.cs_code
            )
        )


class TAtom(Base):
    """
    Symmetry unique T-atom

    Attributes:
      framework_id : int
        id number of the framework
      name : str
        Name of the T-atom
      x : float
        x coordinate
      y : float
        y coordiante
      z : float
        z coordiante
      csq : str
        A string representing the coordination sequence with values separated
        by a pipe '|'
      multiplicity : int
        Site multiplicity
      sym_restrictions : str
        Symmetry restrictions
      site_symmetry : int
        Site symmetry
      vertex_symbol : str
        Vertex symbol
    """

    __tablename__ = "tatoms"

    id = Column(Integer, primary_key=True)
    framework_id = Column(Integer, ForeignKey("frameworks.id"))
    name = Column(String)
    multiplicity = Column(Integer)
    sym_restrictions = Column(String)
    site_symmetry = Column(Integer)
    vertex_symbol = Column(String)
    csq = Column(String)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)

    @hybrid_property
    def xyz(self):
        return np.asarray([self.x, self.y, self.z], dtype=float)

    def coord_seq(self):
        return self.csq.split("|")

    def __repr__(self):
        return "%s(\n%s)" % (
            (self.__class__.__name__),
            " ".join(
                [
                    "\t%s=%r,\n" % (key, getattr(self, key))
                    for key in sorted(self.__dict__.keys())
                    if not key.startswith("_")
                ]
            ),
        )


class Framework(Base):
    """
    Zeolite framework.

    Attributes:
      code : str
        Three letter framework code
      name : str
        Name of the framework
      atoms : int
        Number of atoms in the unit cell
      portals : int
        Number of portals in the unit cell
      channels : int
        Number of channels in the unit cell
      cages : int
        Number of cages in the unit cell
      junctions : int
        Number of junctions in the unit cell
      connections : int
        Number of atom connections in the unit cell
      tpv_abs : float
        Total pore volume in cm^3/g
      tpv_rel : float
        Relative total pore volume,  % of the total volume
      lcd : float
        Largest cavity diameter in Angstrom
      pld : float
        Pore limiting diameter in Angstrom
      a : float
        Unit cell length *a* in Angstrom
      b : float
        Unit cell length *b* in Angstrom
      c : float
        Unit cell length *c* in Angstrom
      alpha : float
        Unit cell angle *alpha* in degrees
      beta : float
        Unit cell angle *beta* in degrees
      gamma : float
        Unit cell angle *gamma* in degrees
      accessible_area : float
        The area of that surface visited by the center of a (spherical) water
        molecule (radius = 1.4 Angstrom) in Angstrom squared [Angstrom^2].
      accessible_area_m2pg : float
        The area of that surface visited by the center of a (spherical) water
        molecule (radius = 1.4 Angstrom) in squared meters per gram [m^2/g].
      accessible_volume : float
        That portion of the occupiable volume that has continuity between all
        unit unit cells. Some pores/cavities have windows that are too small to
        allow the water molecule access, and so represent isolated occupiable
        regions [Angstrom^3].
      accessible_volume_pct : float
        That portion of the occupiable volume that has continuity between all
        unit unit cells. Some pores/cavities have windows that are too small to
        allow the water molecule access, and so represent isolated occupiable
        regions [%].
      channel_dim : int
        Number of dimension of the channel system
      cif : str
        Contents of the CIF file
      framework_density : float
        Frameork density, the number of T-atoms per 1000 Angstrom^3
      isinterrupted : bool
        Flag indicating if the framework type is interrupted
      isdisordered : bool
        Flag indicating if the framework type is disordered
      maxdsd_a : float
        Maximum diameter of a sphere that can diffuse along 'a'
      maxdsd_b : float
        Maximum diameter of a sphere that can diffuse along 'b'
      maxdsd_c : float
        Maximum diameter of a sphere that can diffuse along 'c'
      maxdsi : float
        Maximum diameter of a sphere that can be inlcuded
      occupiable_area : float
        The area of that surface visited by the center of a (sperical) water
        molecule (radius = 1.4 Angstrom) [Angstrom^2]
      occupiable_area_m2pg : float
        The area of that surface visited by the center of a (sperical) water
        molecule (radius = 1.4 Angstrom) [m^2/g]
      occupiable_volume = float
        That portion of the available volume within the cell that can be
        visited by the center of a (spherical) water molecule (radius = 1.4
        Angstrom). The available volume is the unit cell volume remaining after
        the van der Waals atomic sphere volumes are subtracted [Angstrom^3].
      occupiable_volume_pct : float
        That portion of the available volume within the cell that can be
        visited by the center of a (spherical) water molecule (radius = 1.4
        Angstrom). The available volume is the unit cell volume remaining after
        the van der Waals atomic sphere volumes are subtracted [%].
      rdls : float
        R_DLS
      sbu : str
        Secondary building units
      specific_accessible_area : float
        Accessible area per unit volume
      specific_occupiable_area : float
        Occupiable area per unit volume
      td10 : float
        Approximation to the topological density terminated at the 10th item of
        the coordination sequence, see "Atlas of Zeolite Framework Types",
        Ch. Baerlocher, W. M. Meier, D. H. Olson, Fifth Revised Edition, Elsevier
        2001, pp. 17.
      topological_density : float
        Topological density, see "Atlas of Zeolite Framework Types",
        Ch. Baerlocher, W. M. Meier, D. H. Olson, Fifth Revised Edition, Elsevier
        2001, pp. 17.
      url_iza : str
        URL on the IZA website (http://izasc.fos.su.se/fmi/xsl/IZA-SC/ft.xsl)
        from which the relevant data was extracted
      url_zeomics : str
        URL on the ZEOMICS wbesite (http://helios.princeton.edu/zeomics/) from
        which the data was extracted
    """

    __tablename__ = "frameworks"

    id = Column(Integer, primary_key=True)
    # common fields
    code = Column(String)
    # zeomics fileds
    atoms = Column(Integer)
    cages = Column(Integer)
    channels = Column(Integer)
    connections = Column(Integer)
    junctions = Column(Integer)
    lcd = Column(Float)
    name = Column(String)
    pld = Column(Float)
    portals = Column(Integer)
    tpw_abs = Column(Float)
    tpw_pct = Column(Float)
    url_zeomics = Column(String)
    # iza fields
    a = Column(Float)
    b = Column(Float)
    c = Column(Float)
    alpha = Column(Float)
    beta = Column(Float)
    gamma = Column(Float)
    accessible_area = Column(Float)
    accessible_area_m2pg = Column(Float)
    accessible_volume = Column(Float)
    accessible_volume_pct = Column(Float)
    channel_dim = Column(Integer)
    cif = Column(String)
    framework_density = Column(Float)
    isdisordered = Column(Boolean)
    isinterrupted = Column(Boolean)
    maxdsd_a = Column(Float)
    maxdsd_b = Column(Float)
    maxdsd_c = Column(Float)
    maxdsi = Column(Float)
    occupiable_area = Column(Float)
    occupiable_area_m2pg = Column(Float)
    occupiable_volume = Column(Float)
    occupiable_volume_pct = Column(Float)
    rdls = Column(Float)
    sbu = Column(String)
    specific_accessible_area = Column(Float)
    specific_occupiable_area = Column(Float)
    td10 = Column(Float)
    topological_density = Column(Float)
    url_iza = Column(String)

    # many to one relationship
    _spacegroup_id = Column(Integer, ForeignKey("spacegroups.id"))
    speacegroup = relationship("SpaceGroup", uselist=False)

    # many to many relationships
    ring_sizes = relationship("RingSize", secondary=fw_rings, backref="frameworks")
    natural_tilings = relationship(
        "NaturalTiling", secondary=fw_tilings, backref="frameworks"
    )

    # one to many relationship
    tatoms = relationship("TAtom")

    def __repr__(self):
        return "%s(\n%s)" % (
            (self.__class__.__name__),
            " ".join(
                [
                    "\t%s=%r,\n" % (key, getattr(self, key))
                    for key in sorted(self.__dict__.keys())
                    if not key.startswith("_")
                ]
            ),
        )


def cli_getcif():
    "CLI to get the cif files"

    parser = argparse.ArgumentParser()
    parser.add_argument("code", help="Three letter framework code")
    args = parser.parse_args()

    if len(args.code) != 3:
        raise ValueError("Framework error should have three letters")
    else:
        fram = framework(args.code.upper())
        fname = fram.code + ".cif"
        with open(fname, "w") as out:
            out.write(fram.cif)
        print("Wrote to file: {}".format(fname))


def cli_print_framework():
    "CLI interface for getting information about a given framework"

    parser = argparse.ArgumentParser()
    parser.add_argument("code", help="Three letter framework code")
    parser.add_argument("-f", help="Full information")
    args = parser.parse_args()

    if len(args.code) != 3:
        raise ValueError("Framework error should have three letters")
    else:
        f = framework(args.code.upper())

        code = f.code.center(50, "=") + "\n"

        cell = "\n".join(
            [
                "Cell parameters",
                "\ta={a:7.3f} Å  b={b:7.3f} Å  c={c:7.3f} Å".format(
                    a=f.a, b=f.b, c=f.c
                ),
                "\tα={a:7.3f} °  β={b:7.3f} °  γ={c:7.3f} °".format(
                    a=f.alpha, b=f.beta, c=f.gamma
                ),
            ]
        )

        print(code, cell, sep="\n")
