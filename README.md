rpm-ghc
=======

An RPM spec file to build and install the Glasgow Haskell Compiler (GHC).

To Build:

`sudo yum -y install rpmdevtools gmp-devel && rpmdev-setuptree`

`sudo yum -y install gmp-devel glibc-devel ncurses-devel gmp-devel automake libtool gcc44 make perl python libffi-devel ghc-bootstrap-compiler7`

`wget http://www.haskell.org/ghc/dist/7.6.3/ghc-7.6.3-src.tar.bz2 -O ~/rpmbuild/SOURCES/ghc-7.6.3-src.tar.bz2`

`wget https://raw.github.com/nmilford/rpm-ghc/master/ghc.spec -O ~/rpmbuild/SPECS/ghc.spec`

`rpmbuild -bb ~/rpmbuild/SPECS/ghc.spec`
