FROM alpine:latest  
  
LABEL maintainer "Xiaowei Zhan <zhanxw@umich.edu>"  
  
RUN apk update && apk add \  
# General  
wget \  
# Compiler  
gcc \  
g++ \  
gfortran \  
make \  
git \  
# Library  
zlib-dev \  
# Tools for automatic tests  
R R-dev\  
python2 \  
bash  
  
SHELL ["/bin/bash", "-c"]  
  
#setup R configs  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages('testthat')"  
RUN Rscript -e "install.packages('mvtnorm')"  
  
# Get and build RVTESTS  
RUN git clone https://github.com/zhanxw/rvtests.git && \  
cd rvtests && make debug && \  
(for i in base libVcf regression;do make -C ${i}/test; make -C ${i}/test
check; done;)  
  
ENV PATH=/rvtests/executable/dbg:$PATH  
  
WORKDIR /rvtests  

