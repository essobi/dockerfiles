#  
# docker run -ti --rm \  
# germangb/cmatrix "$@"  
#  
FROM ubuntu:trusty  
MAINTAINER germangb <germangb42@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y cmatrix && \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["cmatrix"]  

