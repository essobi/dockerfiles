FROM tupipa/hol4-mosml-base  
  
# STEP 1: install moscow ml from source  
# install packages and clone source code of mosml  
#RUN apt-get update && apt-get install nano git -y \  
# && apt-get install make gcc g++ libgmp3-dev -y \  
# && cd /root \  
# && git clone https://github.com/kfl/mosml \  
# && cd mosml && git checkout master  
  
# install moscow ml  
#RUN cd /root/mosml/src \  
# && make world \  
# && make install  
  
# test moscow ml  
#RUN cd /root/mosml/src/test \  
# && make clean && make && diff result result.ok \  
# && cd /root/mosml/src/mosmllib/test \  
# && make clean \  
# && make \  
# && diff result result.ok \  
# && echo "done testing"  
  
# Note that some of the test cases are suitable only for 32-bit  
# architectures, and will fail on 64-bit architectures (such as DEC  
# Alpha); this does not necessarily indicate that the Moscow ML  
# implementation is broken.  
  
# Done install mosml.  
  
# STEP 2: install HOL4 from source  
# get source code  
RUN cd /root/ \  
&& git clone git://github.com/HOL-Theorem-Prover/HOL.git  
  
# build source code  
RUN cd /root/HOL \  
&& mosml < tools/smart-configure.sml  
RUN cd /root/HOL && ./bin/build  
  
  

