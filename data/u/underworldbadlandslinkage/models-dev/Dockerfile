FROM underworldcode/base:dev  
MAINTAINER Romain Beucher  
  
# set working directory to /root  
WORKDIR /root  
  
# setup environment  
ENV PYTHONPATH $PYTHONPATH:/root/underworld2  
  
RUN mkdir /workspace && \  
mkdir -p /workspace/BADLANDS/companion && \  
mkdir /workspace/UNDERWORLD  
  
# get underworld, compile, delete some unnecessary files, trust notebooks,
copy to workspace  
RUN git clone \--branch "development" \--single-branch
https://github.com/underworldcode/underworld2 && \  
cd underworld2/libUnderworld && \  
./configure.py --with-debugging=0 && \  
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
rm -fr Solvers && \  
find /root/underworld2/docs -name \\*.ipynb -print0 | xargs -0 jupyter trust
&& \  
rsync -av /root/underworld2/docs/examples /workspace/UNDERWORLD && \  
rsync -av /root/underworld2/docs/user_guide /workspace/UNDERWORLD && \  
rsync -av /root/underworld2/docs/publications /workspace/UNDERWORLD && \  
cd ../../docs/development/api_doc_generator/ && \  
sphinx-build . ../../api_doc  
  
RUN pip install git+https://github.com/badlands-model/triangle.git  
RUN pip install pandas  
RUN pip install ez_setup  
RUN pip install gFlex  
  
WORKDIR /root  
RUN git clone https://github.com/badlands-model/pyBadlands.git  
WORKDIR /root/pyBadlands/pyBadlands/libUtils  
RUN make  
RUN pip install -e /root/pyBadlands  
  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/root/pyBadlands/pyBadlands/libUtils  
  
WORKDIR /root  
RUN git clone https://github.com/badlands-model/pyBadlands-Companion.git  
RUN pip install -e /root/pyBadlands-Companion  
RUN rsync -av /root/pyBadlands/Examples/* /workspace/BADLANDS  
RUN rsync -av /root/pyBadlands-Companion/notebooks/*
/workspace/BADLANDS/companion/  
  
# install Linkage  
WORKDIR /root  
RUN git clone
https://2089d41a1b670475f3ac90403ccc37efda43216b@github.com/underworldcode/BasinGenesisHub.git  
RUN pip install -e /root/BasinGenesisHub/linkage/linkagemodel  
  
# expose notebook port  
EXPOSE 8888  
# expose glucifer port  
EXPOSE 9999  
# setup space for working in  
VOLUME /workspace/user_data  
WORKDIR /workspace  
  
# launch notebook  
CMD ["jupyter", "notebook", " --no-browser"]  

