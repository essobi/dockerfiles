FROM ubuntu:16.04  
MAINTAINER webysther@gmail.com  
  
# Update system  
RUN apt-get update && apt-get install -y vim doxygen graphviz  
  
# Added some template  
ADD doxygen/ doxygen/  
  
# Clean cache  
RUN apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /code  
  
ENTRYPOINT ["doxygen", "/doxygen/doxygen.conf"]

