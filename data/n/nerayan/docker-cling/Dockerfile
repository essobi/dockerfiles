# Cling  
#  
# VERSION 0.1.0  
  
FROM ubuntu  
  
RUN apt-get update && apt-get install -y \  
cmake \  
curl \  
g++ \  
git \  
make \  
python \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /opt \  
&& curl -L https://raw.githubusercontent.com/karies/cling-all-in-
one/master/clone.sh \ | bash -ex \  
&& rm -rf obj src  
  
ENTRYPOINT ["/opt/inst/bin/cling"]  

