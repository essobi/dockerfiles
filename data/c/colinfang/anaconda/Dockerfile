# Reference:  
# https://github.com/ContinuumIO/docker-images/blob/master/anaconda/Dockerfile  
# https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook  
# https://github.com/ipython/docker-notebook/tree/master/notebook  
FROM ubuntu  
MAINTAINER Colin Fang <colinfang@live.com>  
  
ENV downloads /downloads  
RUN mkdir $downloads  
  
RUN apt-get update && \  
apt-get install -y wget libglib2.0-0  
ENV anaconda_url
https://repo.continuum.io/archive/Anaconda2-2.5.0-Linux-x86_64.sh  
ENV anaconda_path /opt/anaconda  
ENV PATH $anaconda_path/bin:$PATH  
  
# If we don't do %matplotlib inline,  
# It requires PyQt4 which requires a lot of stuff: ldd
/opt/anaconda/lib/libQtGui.so  
# libgthread-2.0.so.0 -> apt-get install libglib2.0-0  
# libXext.so.6 -> apt-get install libxext6  
# ...  
# Remove cached package tarballs.  
RUN wget -nv -O $downloads/anaconda.sh $anaconda_url && \  
/bin/bash $downloads/anaconda.sh -b -p $anaconda_path && \  
conda update -y conda && \  
conda update -y numpy && \  
conda update -y scipy && \  
conda update -y pandas && \  
rm $downloads/anaconda.sh && \  
conda clean -yt  
  
RUN conda info -a  
RUN ipython -c "print 'Hello World'"

