  
#  
# CentOS 7 (centos7) Devel10 System (dockerfile)  
# Copyright (C) 2016-2017 Stafli  
# Luís Pedro Algarvio  
# This file is part of the Stafli Application Stack.  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
#  
# Build  
#  
# Base image to use  
FROM stafli/stafli.system.base:base10_centos7  
  
# Labels to apply  
LABEL description="Stafli Devel System (stafli/stafli.system.devel), Based on
Stafli Base System (stafli/stafli.system.base" \  
maintainer="lp@algarvio.org" \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.name="Stafli Devel System (stafli/stafli.system.devel)" \  
org.label-schema.description="Based on Stafli Base System
(stafli/stafli.system.base" \  
org.label-schema.keywords="stafli, devel, system, debian, centos, ubuntu,
alpine" \  
org.label-schema.url="https://stafli.org/" \  
org.label-schema.license="GPLv3" \  
org.label-schema.vendor-name="Stafli" \  
org.label-schema.vendor-email="info@stafli.org" \  
org.label-schema.vendor-website="https://www.stafli.org" \  
org.label-schema.authors.lpalgarvio.name="Luis Pedro Algarvio" \  
org.label-schema.authors.lpalgarvio.email="lp@algarvio.org" \  
org.label-schema.authors.lpalgarvio.homepage="https://lp.algarvio.org" \  
org.label-schema.authors.lpalgarvio.role="Maintainer" \  
org.label-schema.registry-
url="https://hub.docker.com/r/stafli/stafli.system.devel" \  
org.label-schema.vcs-url="https://github.com/stafli-org/stafli.system.devel" \  
org.label-schema.vcs-branch="master" \  
org.label-schema.os-id="centos" \  
org.label-schema.os-version-id="7" \  
org.label-schema.os-architecture="amd64" \  
org.label-schema.version="1.0"  
#  
# Arguments  
#  
#  
# Environment  
#  
# Working directory to use when executing build and run instructions  
# Defaults to /.  
#WORKDIR /  
# User and group to use when executing build and run instructions  
# Defaults to root.  
#USER root:root  
#  
# Packages  
#  
# Refresh the package manager  
# Install the selected packages  
# Install the revision control packages  
# - patch: for patch, the patch creator and applier tool  
# - git: for git, the Git distributed revision control system client  
# Install the parser packages  
# - bison: for bison, a YACC-compatible parser generator  
# - m4: for m4, the GNU m4 which is an interpreter for a macro processing
language  
# - re2c: for r2ec, a tool for generating fast C-based recognizers  
# Install the build tools packages  
# - autoconf: for autoconf, a automatic configure script builder for FSF
source packages  
# - automake: for automake, a tool for generating GNU Standards-compliant
Makefiles  
# - make: for make, the GNU make which is an utility for Directing compilation  
# - pkgconfig: for pkg-config, a tool to manage compile and link flags for
libraries  
# - libtool: for GNU libtool, a generic library support script  
# Install the compiler packages  
# - cpp: for cpp, the GNU C preprocessor (cpp) for the C Programming language  
# - gcc: for gcc, the GNU C compiler  
# - gcc-c++: for g++, the GNU C++ compiler  
# Install the library packages  
# - kernel-headers: the Linux Kernel - Headers for development  
# - glibc-headers: the Embedded GNU C Library - Development Libraries and
Header Files  
# - pcre-devel: the Perl 5 Compatible Regular Expression Library - development
files  
# - openssl-devel: the OpenSSL toolkit - development files  
# - gnutls-devel: GNU TLS library - development files  
# - libcurl-devel: the CURL library - development files (OpenSSL version)  
# - cyrus-sasl-devel: the Cyrus SASL library - development files  
# - openldap-devel: the OpenLDAP library - development files  
# - krb5-devel: the MIT Kerberos library - development files  
# - libxml2-devel: the GNOME XML library - development files  
# - zlib-devel: the ZLib library - development files  
# Cleanup the package manager  
RUN printf "Installing repositories and packages...\n" && \  
\  
printf "Refresh the package manager...\n" && \  
rpm --rebuilddb && yum makecache && \  
\  
printf "Install the selected packages...\n" && \  
yum install -y \  
patch git \  
bison m4 re2c \  
autoconf automake make pkgconfig libtool \  
cpp gcc gcc-c++ \  
kernel-headers glibc-headers pcre-devel \  
openssl-devel gnutls-devel libcurl-devel \  
cyrus-sasl-devel openldap-devel krb5-devel \  
libxml2-devel zlib-devel && \  
\  
printf "Cleanup the package manager...\n" && \  
yum clean all && rm -Rf /var/lib/yum/* && rm -Rf /var/cache/yum/* && \  
\  
printf "Finished installing repositories and packages...\n";  
  
#  
# Configuration  
#  
#  
# Run  
#  
# Command to execute  
# Defaults to /bin/bash.  
#CMD ["/bin/bash"]  
# Ports to expose  
# Defaults to none.  
#EXPOSE ...  

