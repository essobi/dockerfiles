FROM ubuntu:latest  
  
# install essential packages  
RUN apt-get update && apt-get install polyml -y \  
&& apt-get install git nano g++ -y \  
# && echo "declare -x LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu " >>
/root/.bashrc \  
# && source /root/.bashrc \  
&& cd /usr/lib/x86_64-linux-gnu/ && ln -s libpolyml.so.7.0.0 libpolyml.so  
  
# get source code  
RUN cd /root/ \  
&& git clone git://github.com/HOL-Theorem-Prover/HOL.git  
  
# build source code  
RUN cd /root/HOL \  
&& echo "val polymllibdir = \"/usr/lib/x86_64-linux-gnu\"" > tools-poly/poly-
includes.ML \  
&& poly < tools/smart-configure.sml \  
&& ./bin/build  

