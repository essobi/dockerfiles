# registry.gitlab.com/jorjpimm/dockerfiles/gcc7_qt  
FROM appcontainers/ubuntu:xenial  
  
WORKDIR /build  
  
ADD tools/install_core_dependencies.sh ./install_core_dependencies.sh  
RUN ./install_core_dependencies.sh  
  
ADD tools/install_python3.sh ./install_python3.sh  
RUN ./install_python3.sh  
  
ADD tools/install_clang.sh ./install_clang.sh  
RUN ./install_clang.sh 4  
  
#ADD tools/install_boost.sh ./install_boost.sh  
#RUN ./install_boost.sh clang  
ADD tools/install_qt.sh ./install_qt.sh  
RUN ./install_qt.sh

