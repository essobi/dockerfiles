FROM opensuse:42.2  
MAINTAINER Matwey V. Kornilov <matwey.kornilov@gmail.com>  
  
ENV CXX g++-4.8  
ENV CC gcc-4.8  
RUN zypper -n ar
'http://download.opensuse.org/repositories/devel:/gcc/openSUSE_Leap_42.2/devel:gcc.repo'  
RUN zypper -n ar
'http://download.opensuse.org/repositories/KDE:/Qt56/openSUSE_Leap_42.2/KDE:Qt56.repo'  
  
RUN zypper -n --gpg-auto-import-keys install --no-recommends --auto-agree-
with-licenses --force-resolution cmake make libQt5Widgets-devel libQt5Test-
devel libQt5Gui-devel libQt5Core-devel gcc48-c++

