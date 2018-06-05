FROM underworldbadlandslinkage/linkage-base  
  
MAINTAINER Ian Howson  
  
WORKDIR /build  
RUN git clone https://github.com/badlands-model/pyBadlands.git  
WORKDIR /build/pyBadlands/pyBadlands/libUtils  
RUN make  
RUN pip install -e /build/pyBadlands  
  
WORKDIR /build  
RUN git clone https://github.com/badlands-model/pyBadlands-Companion.git  
RUN pip install -e /build/pyBadlands-Companion  
  
# get underworld, compile, delete some unnecessary files, trust notebooks,
copy to workspace  
WORKDIR /build  
RUN git clone \--branch "master" \--single-branch
https://github.com/underworldcode/underworld2 && \  
cd underworld2/libUnderworld && \  
./configure.py --with-debugging=1 && \  
./compile.py && \  
rm .sconsign.dblite && \  
rm -fr .sconf_temp && \  
cd build && \  
rm -fr libUnderworldPy && \  
rm -fr StGermain && \  
rm -fr gLucifer && \  
rm -fr Underworld && \  
rm -fr StgFEM && \  
rm -fr StgDomain && \  
rm -fr PICellerator && \  
rm -fr Solvers  
  
# install Linkage  
WORKDIR /build  
RUN git clone
https://2089d41a1b670475f3ac90403ccc37efda43216b@github.com/underworldcode/BasinGenesisHub.git  
RUN pip install -e /build/BasinGenesisHub/linkage/linkagemodel  
  

