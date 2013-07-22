# To Build:
# sudo yum -y install rpmdevtools gmp-devel && rpmdev-setuptree
# sudo yum -y install gmp-devel glibc-devel ncurses-devel  gmp-devel automake libtool gcc44 make  perl python libffi-devel ghc-bootstrap-compiler7
# wget http://www.haskell.org/ghc/dist/7.0.2/ghc-7.0.2-src.tar.bz2 -O ~/rpmbuild/SOURCES/ghc-7.0.2-src.tar.bz2
# wget https://raw.github.com/nmilford/rpm-ghc-bootsrap-compiler7/master/ghc-bootsrap-compiler7.spec -O ~/rpmbuild/SPECS/ghc-bootsrap-compiler7.spec
# rpmbuild -bb ~/rpmbuild/SPECS/ghc-bootsrap-compiler7.spec

%define ghc_bootstrap_ver 7.0.2
%define ghc_bootstrap_pkg ghc-bootstrap-compiler7

Name:           ghc
Version:        7.6.3
Release:        1
Summary:        The Glorious Glasgow Haskell Compilation System
Group:          Development/Languages
License:        The Glasgow Haskell Compiler License
URL:            http://www.haskell.org/ghc/
Source0:        http://www.haskell.org/ghc/dist/%{version}/ghc-%{version}-src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:   %{ghc_bootstrap_pkg}
BuildRequires:   gmp-devel
BuildRequires:   glibc-devel
BuildRequires:   ncurses-devel
BuildRequires:   gmp-devel
BuildRequires:   automake
BuildRequires:   libtool
BuildRequires:   gcc44
BuildRequires:   make
BuildRequires:   perl
BuildRequires:   python
BuildRequires:   libffi-devel

%description
GHC is a state-of-the-art, open source, compiler and interactive environment
for the functional language Haskell. Highlights:

- GHC supports the entire Haskell 2010 language plus various extensions.
- GHC has particularly good support for concurrency and parallelism,
  including support for Software Transactional Memory (STM).
- GHC generates fast code, particularly for concurrent programs
  (check the results on the "Computer Language Benchmarks Game").
- GHC works on several platforms including Windows, Mac, Linux,
  most varieties of Unix, and several different processor architectures.
- GHC has extensive optimisation capabilities,
  including inter-module optimisation.
- GHC compiles Haskell code either directly to native code or using LLVM
  as a back-end. GHC can also generate C code as an intermediate target for
  porting to new platforms. The interactive environment compiles Haskell to
  bytecode, and supports execution of mixed bytecode/compiled programs.
- Profiling is supported, both by time/allocation and heap profiling.
- GHC comes with core libraries, and thousands more are available on Hackage.

%prep
%setup -q -n ghc-%{version}

%build
./configure --with-ghc=/usr/bin/ghc-%{ghc_bootstrap_ver} --with-gcc=/usr/bin/gcc44

make 

%install
install -d -m 755 %{buildroot}/usr/

%makeinstall
install -d -m 755 %{buildroot}/usr/share/doc/ghc-%{version}
install    -m 644 %{_builddir}/ghc-%{version}/README  %{buildroot}/usr/share/doc/ghc-%{version}
install    -m 644 %{_builddir}/ghc-%{version}/LICENSE %{buildroot}/usr/share/doc/ghc-%{version}

for file in ghc-%{version} ghci-%{version} ghc-pkg-%{version} haddock-ghc-%{version} hp2ps hpc hsc2hs runghc-%{version}; do
  sed -i -e  's|%{buildroot}||g' %{buildroot}%{_bindir}/$file
done

cd %{buildroot}/%{_libdir}/ghc-%{version}/package.conf.d/
for pkg in *; do
  sed -i -e  's|%{buildroot}||g' $pkg
done
cd -

%post
%{_bindir}/ghc-pkg-%{version} recache

%files
%defattr(-,root,root)
%{_libdir}/ghc*
%{_bindir}/*
/usr/share/doc/*
/usr/share/man/*

%changelog
* Mon Jul 08 2013 Nathan Milford <nathan@milford.io> 7.6.3-1
- Initial spec.
- This is specifically meant to build newer versions of GHC.
