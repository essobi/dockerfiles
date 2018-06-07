FROM ingomuellernet/buildenv  
MAINTAINER Ingo Müller <ingo.mueller@inf.ethz.ch>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libgraphviz-dev \  
python3-pip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --upgrade \  
pylint \  
autopep8 \  
&& rm -r ~/.cache/pip  
  
RUN pip3 install --upgrade \  
cffi \  
dask \  
jsonmerge \  
matplotlib \  
numba \  
numpy \  
pandas \  
pyspark \  
scipy \  
sklearn \  
&& rm -r ~/.cache/pip  

