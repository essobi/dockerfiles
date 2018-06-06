FROM fedora:27  
LABEL maintainer="Ian Hattendorf <ian@ianhattendorf.com>"  
  
RUN set -eux; \  
dnf install -y git curl make cmake meson pkgconf-pkg-config clang clang-tools-
extra clang-analyzer gcc lcov libasan libubsan libtsan findutils valgrind; \  
dnf clean all  
  

