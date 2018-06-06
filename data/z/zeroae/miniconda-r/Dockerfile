FROM continuumio/miniconda  
  
# By keeping a lot of discrete steps in a single RUN we can clean up after  
# ourselves in the same layer. This is gross but it saves space  
RUN set -ex \  
&& apt-get update -yqq \  
&& apt-get install -y lsb-release binutils \  
&& apt-get install -y libc-dev libcloog-isl4 libmpfr4 libmpc3 make \  
&& apt-get install -y vim \  
# \  
# update conda \  
&& conda update conda -y \  
# \  
# create r environment \  
&& conda create -y -n r -c r gcc openjdk r-base r-rjava \  
&& conda clean --tarballs --packages \  
# \  
# javareconf R \  
&& bash -c 'source activate r && R CMD javareconf' \  
# \  
# clean up to minimize image layer size \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $buildDeps  

