FROM ruimashita/numpy  
  
MAINTAINER takuya.wakisaka@moldweorp.com  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libhdf5-dev \  
  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
  
RUN pip install --no-cache-dir h5py chainer  

