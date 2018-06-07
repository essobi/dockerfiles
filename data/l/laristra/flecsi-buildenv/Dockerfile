FROM ubuntu:latest  
RUN apt-get -q update -y  
RUN apt-get -qq install -y make cmake automake autoconf libtool cmake-data git
g++ gfortran flex doxygen graphviz pandoc python2.7 libmpich-dev
libhdf5-mpich-dev libcereal-dev liblapacke-dev libexodusii-dev libscotch-dev
libmetis-dev python-pip texlive-font-utils clang llvm ccache texlive-latex-
base texlive-fonts-recommended texlive-latex-recommended gdb wget curl lcov
libboost-all-dev  
RUN wget -O /usr/bin/doxy-coverage
https://raw.githubusercontent.com/alobbs/doxy-coverage/master/doxy-coverage.py  
RUN chmod +x /usr/bin/doxy-coverage  
  
RUN groupadd -r flecsi  
RUN useradd -r -m -g flecsi flecsi  
USER flecsi  
ENV PATH=/usr/lib/ccache:${PATH}${PATH:+:}  
ENV MPICH=true  
WORKDIR /home/flecsi  
RUN pip install --user codecov coverxygen  

