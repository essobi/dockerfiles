FROM ubuntu:xenial  
LABEL maintainer "tsubasatakayama511@gmail.com"  
  
RUN apt-get update && \  
apt-get install -y \  
cloud-utils && \  
apt-get clean  
  
ENTRYPOINT ["write-mime-multipart"]  
CMD ["--help"]  

