FROM ubuntu:14.04  
MAINTAINER r.dahlen@gmail.com  
  
RUN apt-get update && \  
apt-get install -y -q rsync python-pip && \  
pip install awscli  
  
ADD clojars-s3-sync.sh /bin/clojars-s3-sync  
  
VOLUME /clojars  
  
WORKDIR /clojars  
  
CMD /bin/clojars-s3-sync  

