FROM debian  
  
RUN apt-get update \  
&& apt-get install -y \  
libgmp3-dev \  
libffi-dev \  
libssl-dev \  
python-pip \  
python-dev \  
python-setuptools \  
rng-tools  
  
RUN pip install --upgrade pip \  
&& pip install --upgrade setuptools \  
&& pip install blockstack \  
&& pip install functools32 \  
&& pip install base58 \  
&& pip install cachetools  
  
CMD /bin/bash

