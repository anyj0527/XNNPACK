Name:           XNNPACK
Summary:        XNNPACK
Version:        0.0.1
Release:        1
License:        BSD
Source0:        %{name}-%{version}.tar.gz
Source1001:     XNNPACK.manifest
Source1002:     XNNPACK.pc.in
Source2001:     fxdiv.tar.gz
Source2002:     pthreadpool.tar.gz
Source2003:     clog.tar.gz
Source2004:     cpuinfo.tar.gz
Source2005:     fp16.tar.gz
Source2006:     psimd.tar.gz

BuildRequires: cmake
# BuildRequires: ninja

%description
THIS IS XNNPACK

%package devel
Summary: XNNPACK development headers and object file

%description devel
XNNPACK headers and static library

%prep
%setup -q
cp %{SOURCE1001} .
mkdir -p externals
pushd externals
cp %{SOURCE2001} .
cp %{SOURCE2002} .
cp %{SOURCE2003} .
cp %{SOURCE2004} .
cp %{SOURCE2005} .
cp %{SOURCE2006} .
popd

%build
mkdir -p build
pushd build

EXTRA_CFLAGS="${CFLAGS}"
EXTRA_CXXFLAGS="${CXXFLAGS}"

# %ifarch %arm aarch64
#   EXTRA_CFLAGS="${EXTRA_CFLAGS} -funsafe-math-optimizations"
#   EXTRA_CXXFLAGS="${EXTRA_CXXFLAGS} -funsafe-math-optimizations"
#   %ifarch %arm
#     EXTRA_CFLAGS="${EXTRA_CFLAGS} -mno-unaligned-access"
#     EXTRA_CXXFLAGS="${EXTRA_CXXFLAGS} -mno-unaligned-access"
#   %endif
#   %ifarch armv7l
#     EXTRA_CFLAGS="${EXTRA_CFLAGS} -mfloat-abi=softfp -march=armv7-a -mfpu=neon-vfpv4 -funsafe-math-optimizations -mfp16-format=ieee"
#     EXTRA_CXXFLAGS="${EXTRA_CXXFLAGS} -mfloat-abi=softfp -march=armv7-a -mfpu=neon-vfpv4 -funsafe-math-optimizations -mfp16-format=ieee"
#     # There is bug in toolchain to build XNNPACK for armv7l, so disable it.
#     # See https://github.com/google/XNNPACK/issues/1465 for details.
#     # I guess https://gcc.gnu.org/git/?p=gcc.git;a=commitdiff;h=c1cdabe3aab817d95a8db00a8b5e9f6bcdea936f;hp=6a37d0331c25f23628d4308e5a75624005c223b2 would fix this problem...?
#     # Note that in armv7hl, the build succeed.
#     USE_XNNPACK="OFF"
#   %endif
# %endif

cmake \
  -DCMAKE_C_FLAGS="${EXTRA_CFLAGS}" \
  -DCMAKE_CXX_FLAGS="${EXTRA_CXXFLAGS}" \
  -DXNNPACK_BUILD_TESTS=OFF \
  -DXNNPACK_BUILD_BENCHMARKS=OFF \
  -DXNNPACK_ENABLE_ARM_BF16=OFF \
  ../

cmake --build . %{?_smp_mflags}

popd

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_includedir}/xnnpack

cp %{SOURCE1002} .
sed -i 's:@libdir@:%{_libdir}:g
    s:@includedir@:%{_includedir}/xnnpack/:g' ./XNNPACK.pc.in

# Put the generated files into the buildroot folder
## install built static library
install -m 0644 ./build/libXNNPACK.a %{buildroot}%{_libdir}/libXNNPACK.a

## install headers
pushd include
find . -name "*.h" -type f -exec cp --parents {} %{buildroot}%{_includedir}/xnnpack \;
popd

## install pc file
install -m 0644 XNNPACK.pc.in %{buildroot}%{_libdir}/pkgconfig/XNNPACK.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%manifest XNNPACK.manifest
%license LICENSE
%{_libdir}/libXNNPACK.a
%{_libdir}/pkgconfig/XNNPACK.pc
%{_includedir}/xnnpack

%changelog
* Fri May 27 2022 Yongjoo Ahn <yongjoo1.ahn@samsung.com>
 - Initial package to XNNPACK
