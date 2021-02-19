#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmsh
Version  : 4.6.0
Release  : 9
URL      : https://gmsh.info/src/gmsh-4.6.0-source.tgz
Source0  : https://gmsh.info/src/gmsh-4.6.0-source.tgz
Source1  : gmsh.desktop
Summary  : A three-dimensional finite element mesh generator.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause-LBNL GPL-2.0 GPL-3.0 LGPL-2.1 PostgreSQL
Requires: gmsh-bin = %{version}-%{release}
Requires: gmsh-data = %{version}-%{release}
Requires: gmsh-lib = %{version}-%{release}
Requires: gmsh-license = %{version}-%{release}
Requires: gmsh-man = %{version}-%{release}
Requires: gmsh-openmpi = %{version}-%{release}
Requires: gmsh-python = %{version}-%{release}
Requires: gmsh-python3 = %{version}-%{release}
BuildRequires : CGNS-dev
BuildRequires : OpenCASCADE-dev
BuildRequires : apache-ant
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cairo-dev
BuildRequires : cmake
BuildRequires : flex-dev
BuildRequires : fltk-dev
BuildRequires : freetype-dev
BuildRequires : git
BuildRequires : glu-dev
BuildRequires : gmp-dev
BuildRequires : hdf5-dev
BuildRequires : libMED-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : mesa-dev
BuildRequires : metis-dev
BuildRequires : modules
BuildRequires : openblas
BuildRequires : openjdk11
BuildRequires : openjdk11-dev
BuildRequires : openmpi-dev
BuildRequires : openssh
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : requests
BuildRequires : swig
BuildRequires : zlib-dev
Patch1: 0001-cflags.patch

%description
Gmsh is an open source 3D finite element mesh generator with a built-in CAD engine
and post-processor. Its design goal is to provide a fast, light and user-friendly
meshing tool with parametric input and advanced visualization capabilities.
Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively using
the graphical user interface, in ASCII text files using Gmsh's own scripting language
(.geo files), or using the C++, C, Python or Julia Application Programming Interface (API).

%package bin
Summary: bin components for the gmsh package.
Group: Binaries
Requires: gmsh-data = %{version}-%{release}
Requires: gmsh-license = %{version}-%{release}

%description bin
bin components for the gmsh package.


%package data
Summary: data components for the gmsh package.
Group: Data

%description data
data components for the gmsh package.


%package dev
Summary: dev components for the gmsh package.
Group: Development
Requires: gmsh-lib = %{version}-%{release}
Requires: gmsh-bin = %{version}-%{release}
Requires: gmsh-data = %{version}-%{release}
Requires: gmsh-openmpi = %{version}-%{release}
Provides: gmsh-devel = %{version}-%{release}
Requires: gmsh = %{version}-%{release}

%description dev
dev components for the gmsh package.


%package doc
Summary: doc components for the gmsh package.
Group: Documentation
Requires: gmsh-man = %{version}-%{release}

%description doc
doc components for the gmsh package.


%package lib
Summary: lib components for the gmsh package.
Group: Libraries
Requires: gmsh-data = %{version}-%{release}
Requires: gmsh-license = %{version}-%{release}

%description lib
lib components for the gmsh package.


%package license
Summary: license components for the gmsh package.
Group: Default

%description license
license components for the gmsh package.


%package man
Summary: man components for the gmsh package.
Group: Default

%description man
man components for the gmsh package.


%package openmpi
Summary: openmpi components for the gmsh package.
Group: Default

%description openmpi
openmpi components for the gmsh package.


%package python
Summary: python components for the gmsh package.
Group: Default
Requires: gmsh-python3 = %{version}-%{release}

%description python
python components for the gmsh package.


%package python3
Summary: python3 components for the gmsh package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gmsh package.


%prep
%setup -q -n gmsh-4.6.0-source
cd %{_builddir}/gmsh-4.6.0-source
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607983332
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DENABLE_OPENMP=ON \
-DENABLE_SYSTEM_CONTRIB=YES \
-DENABLE_PRIVATE_API=NO \
-DENABLE_BUILD_LIB=YES \
-DENABLE_BUILD_SHARED=YES \
-DENABLE_BUILD_DYNAMIC=YES \
-DENABLE_MPEG_ENCODE=NO \
-DENABLE_METIS=YES \
-DENABLE_BLOSSOM=YES \
-DENABLE_CGNS=YES \
-DENABLE_MED=YES \
-DENABLE_OCC=YES
make  %{?_smp_mflags}
popd
mkdir -p clr-build-openmpi
pushd clr-build-openmpi
. /usr/share/defaults/etc/profile.d/modules.sh
module load openmpi
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
export FCFLAGS="$FCFLAGS -march=haswell -m64"
export FFLAGS="$FFLAGS -march=haswell -m64"
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=$MPI_ROOT -DCMAKE_INSTALL_SBINDIR=$MPI_BIN \
-DCMAKE_INSTALL_LIBDIR=$MPI_LIB -DCMAKE_INSTALL_INCLUDEDIR=$MPI_INCLUDE -DLIB_INSTALL_DIR=$MPI_LIB \
-DBUILD_SHARED_LIBS:BOOL=ON -DLIB_SUFFIX=64 \
-DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
 .. -DCMAKE_INSTALL_BINDIR=$MPI_BIN \
-DCMAKE_INSTALL_LIBDIR=$MPI_LIB \
-DCMAKE_INSTALL_INCLUDEDIR=$MPI_INCLUDE \
-DENABLE_MPI=YES \
-DENABLE_OPENMP=ON \
-DENABLE_SYSTEM_CONTRIB=YES \
-DENABLE_PRIVATE_API=NO \
-DENABLE_BUILD_LIB=YES \
-DENABLE_BUILD_SHARED=YES \
-DENABLE_BUILD_DYNAMIC=YES \
-DENABLE_MPEG_ENCODE=NO \
-DENABLE_METIS=YES \
-DENABLE_BLOSSOM=YES \
-DENABLE_CGNS=YES \
-DENABLE_MED=YES \
-DENABLE_OCC=YES
make  %{?_smp_mflags}
module unload openmpi
popd

%install
export SOURCE_DATE_EPOCH=1607983332
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gmsh
cp %{_builddir}/gmsh-4.6.0-source/LICENSE.txt %{buildroot}/usr/share/package-licenses/gmsh/dbe2024835d6ed5e4240eec606ed656247a78b1c
cp %{_builddir}/gmsh-4.6.0-source/contrib/ANN/Copyright.txt %{buildroot}/usr/share/package-licenses/gmsh/20adfc29688bd1c919d4a6257083f48ca32e6762
cp %{_builddir}/gmsh-4.6.0-source/contrib/ANN/License.txt %{buildroot}/usr/share/package-licenses/gmsh/b3225b981f5cc501b08289f989e8fb4cde208598
cp %{_builddir}/gmsh-4.6.0-source/contrib/MathEx/license.txt %{buildroot}/usr/share/package-licenses/gmsh/1b10da150f8acd92e45dc8454a4d80b29acb2f90
cp %{_builddir}/gmsh-4.6.0-source/contrib/Netgen/LICENSE %{buildroot}/usr/share/package-licenses/gmsh/e3c201d5ec0b1d34403a209120ffbe44fee51337
cp %{_builddir}/gmsh-4.6.0-source/contrib/hxt/LICENSE.txt %{buildroot}/usr/share/package-licenses/gmsh/11aa6b73eebba1fd04f2008fd88e7135a3049b49
cp %{_builddir}/gmsh-4.6.0-source/contrib/kbipack/LICENSE %{buildroot}/usr/share/package-licenses/gmsh/8b6e6298dbea901e1d36e2693ca209cc9afaa75c
cp %{_builddir}/gmsh-4.6.0-source/contrib/metis/LICENSE.txt %{buildroot}/usr/share/package-licenses/gmsh/a7c3a4f7dcf7a014c7dfdd3f8752d699eb7f7c2e
cp %{_builddir}/gmsh-4.6.0-source/contrib/mmg3d/LICENCE.txt %{buildroot}/usr/share/package-licenses/gmsh/bae38323d3b5434e05112d3f3dfc05287ddc93f5
cp %{_builddir}/gmsh-4.6.0-source/contrib/mpeg_encode/COPYRIGHT.txt %{buildroot}/usr/share/package-licenses/gmsh/b9bb073a06d409c357d96e3616fb3c0fbc25a530
cp %{_builddir}/gmsh-4.6.0-source/contrib/voro++/LICENSE %{buildroot}/usr/share/package-licenses/gmsh/39d1b08cdc31ab93d272c7377e2fc4ca635068a4
cp %{_builddir}/gmsh-4.6.0-source/utils/pypi/gmsh-dev/LICENSE %{buildroot}/usr/share/package-licenses/gmsh/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/gmsh-4.6.0-source/utils/pypi/gmsh/LICENSE %{buildroot}/usr/share/package-licenses/gmsh/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build-openmpi
module load openmpi
%make_install_openmpi
module unload openmpi
popd
pushd clr-build
%make_install
popd
mkdir -p %{buildroot}/usr/share/applications
install  %{_sourcedir}/gmsh.desktop %{buildroot}/usr/share/applications/
## install_append content
sitedir=$(python -c "import sys; print(sys.path[-1])")

mkdir -p %{buildroot}/usr/share/gmsh
mv %{buildroot}/usr/lib64/gmsh.jl %{buildroot}/usr/share/gmsh/
mkdir -p %{buildroot}/$sitedir
mv %{buildroot}/usr/bin/onelab.py %{buildroot}/$sitedir/
mv %{buildroot}/usr/lib64/gmsh.py %{buildroot}/$sitedir/

mpi_sitedir=${sitedir#/usr}
module load openmpi
mkdir -p %{buildroot}/$MPI_ROOT/share/gmsh
mv %{buildroot}/usr/lib64/openmpi/lib/gmsh.jl %{buildroot}/$MPI_ROOT/share/gmsh/
mkdir -p %{buildroot}/$MPI_ROOT/$mpi_sitedir
mv %{buildroot}/$MPI_ROOT/bin/onelab.py %{buildroot}/$MPI_ROOT/$mpi_sitedir/
mv %{buildroot}/$MPI_ROOT/lib/gmsh.py %{buildroot}/$MPI_ROOT/$mpi_sitedir/
module unload openmpi

# Install icon
install -Dpm 0644 utils/icons/gmsh.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/gmsh.svg
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gmsh

%files data
%defattr(-,root,root,-)
/usr/share/applications/gmsh.desktop
/usr/share/gmsh/gmsh.jl
/usr/share/icons/hicolor/scalable/apps/gmsh.svg

%files dev
%defattr(-,root,root,-)
/usr/include/gmsh.h
/usr/include/gmsh.h_cwrap
/usr/include/gmshc.h
/usr/lib64/libgmsh.so
/usr/lib64/openmpi/include/gmsh.h
/usr/lib64/openmpi/include/gmsh.h_cwrap
/usr/lib64/openmpi/include/gmshc.h
/usr/lib64/openmpi/lib/libgmsh.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gmsh/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgmsh.so.4.6
/usr/lib64/libgmsh.so.4.6.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gmsh/11aa6b73eebba1fd04f2008fd88e7135a3049b49
/usr/share/package-licenses/gmsh/1b10da150f8acd92e45dc8454a4d80b29acb2f90
/usr/share/package-licenses/gmsh/20adfc29688bd1c919d4a6257083f48ca32e6762
/usr/share/package-licenses/gmsh/39d1b08cdc31ab93d272c7377e2fc4ca635068a4
/usr/share/package-licenses/gmsh/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gmsh/8b6e6298dbea901e1d36e2693ca209cc9afaa75c
/usr/share/package-licenses/gmsh/a7c3a4f7dcf7a014c7dfdd3f8752d699eb7f7c2e
/usr/share/package-licenses/gmsh/b3225b981f5cc501b08289f989e8fb4cde208598
/usr/share/package-licenses/gmsh/b9bb073a06d409c357d96e3616fb3c0fbc25a530
/usr/share/package-licenses/gmsh/bae38323d3b5434e05112d3f3dfc05287ddc93f5
/usr/share/package-licenses/gmsh/dbe2024835d6ed5e4240eec606ed656247a78b1c
/usr/share/package-licenses/gmsh/e3c201d5ec0b1d34403a209120ffbe44fee51337

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gmsh.1

%files openmpi
%defattr(-,root,root,-)
/usr/lib64/openmpi/bin/gmsh
/usr/lib64/openmpi/lib/libgmsh.so.4.6
/usr/lib64/openmpi/lib/libgmsh.so.4.6.0
/usr/lib64/openmpi/lib/python3.9/site-packages/gmsh.py
/usr/lib64/openmpi/lib/python3.9/site-packages/onelab.py
/usr/lib64/openmpi/share/doc/gmsh/CHANGELOG.txt
/usr/lib64/openmpi/share/doc/gmsh/CREDITS.txt
/usr/lib64/openmpi/share/doc/gmsh/LICENSE.txt
/usr/lib64/openmpi/share/doc/gmsh/README.txt
/usr/lib64/openmpi/share/doc/gmsh/demos/api/CMakeLists.txt
/usr/lib64/openmpi/share/doc/gmsh/demos/api/README.txt
/usr/lib64/openmpi/share/doc/gmsh/demos/api/adapt_mesh.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/adapt_mesh.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/as1-tu-203.stp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/bgmesh.pos
/usr/lib64/openmpi/share/doc/gmsh/demos/api/boolean.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/boolean.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/bspline_bezier_patches.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/bspline_filling.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/closest_point.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/crack.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/custom_gui.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/custom_gui.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/discrete.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/discrete.jl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/discrete.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/edges.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/explore.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/explore.jl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/explore.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/faces.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/flatten.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/glue_and_remesh_stl.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/gui.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/gui.jl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/gui.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/heal.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/hex.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/mesh_from_discrete_curve.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/neighbors.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/normals.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/object.stl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/onelab_data.c
/usr/lib64/openmpi/share/doc/gmsh/demos/api/onelab_data.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/onelab_data.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/onelab_test.jl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/onelab_test.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/open.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/open.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/opt.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/partition.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/partition.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/perf.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/perf.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/periodic.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/plugin.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/plugin.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/poisson.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/remesh_stl.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/reparamOnFace.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/simple.c
/usr/lib64/openmpi/share/doc/gmsh/demos/api/simple.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/simple.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/spherical_surf.jl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/spherical_surf.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/spline.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/spline.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/square.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/square.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/api/step_assembly.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/step_boundary_colors.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/step_boundary_colors.stp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/surface1.stl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/surface2.stl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/terrain.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/terrain_stl.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/terrain_stl_data.stl
/usr/lib64/openmpi/share/doc/gmsh/demos/api/test.c
/usr/lib64/openmpi/share/doc/gmsh/demos/api/test.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/view.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/view.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/view_combine.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/viewlist.cpp
/usr/lib64/openmpi/share/doc/gmsh/demos/api/viewlist.py
/usr/lib64/openmpi/share/doc/gmsh/demos/api/volume.py
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/as1-tu-203.stp
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/baffles.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/boolean.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/chamfer.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/coherence.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/component8.step
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/compsolid.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/compsolid2.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/extrude.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/extrude2.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/fillet.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/fillet2.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/fillet3.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/fillet4.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/fillet_chamfer.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/fragment_numbering.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/hybrid_occ_builtin.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/import.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/import2.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/intersect_line_volume.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/neuron.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/periodic.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/periodic_embedded.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/pipe.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/primitives.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/revolve.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/revolve2.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/shell_sewing.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/simple.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/simple2.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/simple3.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/simple4.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/simple5.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/simple6.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/simple7.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/slicer.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/slicer_surfaces.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/spherical_surf.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/spline.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/step_assembly.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/surface_filling.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/thicksolid.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/thrusections.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/transfinite.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/transform.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/boolean/twist.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/anim.script
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/compute_area_volume.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/encode.script
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/isosurf.script
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/lowmem-anim.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/multislice.script
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/plot2d.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/primitives.pos
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/rotate.script
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/title.script
/usr/lib64/openmpi/share/doc/gmsh/demos/post_processing/view_groups.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/antenna.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/antenna.i1
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/cone.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/cube.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/filter.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/hex.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/homology.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/indheat.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/machine.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/machine.i1
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/machine.i2
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/piece-extr-rec.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/piece-extr.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/piece.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/pripyrtet.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/sphere-discrete.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/sphere-surf.stl
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/sphere.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/splines.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/square_regular.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/tower.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/tower.i1
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/tower.i2
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/tower.i3
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/tower.i4
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/tower.i5
/usr/lib64/openmpi/share/doc/gmsh/demos/simple_geo/transfinite.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/struct/Exists_GetForced.geo
/usr/lib64/openmpi/share/doc/gmsh/demos/struct/struct.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/README.txt
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/README.txt
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t1.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t10.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t11.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t12.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t13.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t14.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t15.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t16.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t17.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t18.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t19.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t2.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t20.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t21.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t3.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t4.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t5.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t6.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t7.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t8.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/t9.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/x1.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c++/x2.cpp
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c/README.txt
/usr/lib64/openmpi/share/doc/gmsh/tutorial/c/t1.c
/usr/lib64/openmpi/share/doc/gmsh/tutorial/julia/README.txt
/usr/lib64/openmpi/share/doc/gmsh/tutorial/julia/t1.jl
/usr/lib64/openmpi/share/doc/gmsh/tutorial/julia/t16.jl
/usr/lib64/openmpi/share/doc/gmsh/tutorial/julia/t2.jl
/usr/lib64/openmpi/share/doc/gmsh/tutorial/julia/t3.jl
/usr/lib64/openmpi/share/doc/gmsh/tutorial/julia/t4.jl
/usr/lib64/openmpi/share/doc/gmsh/tutorial/julia/t5.jl
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/README.txt
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t1.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t10.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t11.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t12.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t13.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t14.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t15.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t16.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t17.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t18.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t19.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t2.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t20.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t21.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t3.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t4.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t5.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t6.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t7.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t8.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/t9.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/x1.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/python/x2.py
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t1.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t10.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t11.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t12.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t13.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t13_data.stl
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t14.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t15.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t16.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t17.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t17_bgmesh.pos
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t18.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t19.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t2.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t20.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t20_data.step
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t21.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t3.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t4.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t4_image.png
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t5.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t6.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t7.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t7_bgmesh.pos
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t8.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/t9.geo
/usr/lib64/openmpi/share/doc/gmsh/tutorial/view1.pos
/usr/lib64/openmpi/share/doc/gmsh/tutorial/view2.pos
/usr/lib64/openmpi/share/doc/gmsh/tutorial/view3.pos
/usr/lib64/openmpi/share/doc/gmsh/tutorial/view4.pos
/usr/lib64/openmpi/share/doc/gmsh/tutorial/view5.msh
/usr/lib64/openmpi/share/gmsh/gmsh.jl
/usr/lib64/openmpi/share/man/man1/gmsh.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
