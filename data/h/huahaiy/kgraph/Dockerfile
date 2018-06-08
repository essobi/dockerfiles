#  
# Run kgraph KNN search service on HTTP  
#  
# Version 0.2  
#  
FROM huahaiy/debian  
  
MAINTAINER Huahai Yang <hyang@juji-inc.com>  
  
ADD kgraph /opt/kgraph  
  
ADD index.py /usr/bin/index.py  
ADD search.py /usr/bin/search.py  
  
RUN \  
echo "===> install dependencies..." && \  
apt-get update && \  
apt-get install -y --force-yes build-essential git libboost-timer-dev \  
libboost-chrono-dev libboost-program-options-dev libboost-system-dev \  
libboost-python-dev python-numpy python-setuptools libopenblas-dev && \  
easy_install wheezy.web  
  
RUN \  
echo "===> build " && \  
cd /opt/kgraph && \  
sed -i 's/libblas/libopenblas/' /opt/kgraph/python/Makefile && \  
make && \  
make install && \  
make clean && \  
\  
\  
echo "===> clean up..." && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV KGRAPH_DATA /kgraph  
  
EXPOSE 8071  
VOLUME ["/kgraph"]  

