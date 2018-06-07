FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
python-pip \  
git \  
gcc \  
python-dev \  
libffi-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev  
  
RUN pip install --upgrade pip setuptools  
  
#RUN pip install -r tools/optional-requires  
RUN pip install ryu  
  
#RUN pip install -r tools/optional-requires  
WORKDIR /tmp  
  
RUN git clone git://github.com/osrg/ryu.git /tmp/ryu  
  
WORKDIR /tmp/ryu  
  
RUN python ./setup.py install  

