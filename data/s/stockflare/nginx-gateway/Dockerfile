FROM nginx:1.9.4  
MAINTAINER David Kelley <david@stockflare.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV LISTEN_ON 2345  
ENV CONFD_VERSION 0.10.0  
ADD etc/confd /etc/confd  
  
ADD certs /certs  
  
ADD confd/confd-0.10.0-linux-amd64 /bin/confd  
  
WORKDIR /nginx  
  
RUN apt-get update && apt-get install -y python curl && curl -O
https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && pip install awscli  
  
ADD boot boot  
  
CMD ["./boot"]  

