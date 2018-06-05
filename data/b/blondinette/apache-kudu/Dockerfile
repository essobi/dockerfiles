FROM ubuntu:xenial  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get -y install apt-utils wget dstat aptitude ntp  
  
# Install repository and gpg key  
WORKDIR /etc/apt/sources.list.d  
RUN wget
https://archive.cloudera.com/kudu/ubuntu/xenial/amd64/kudu/archive.key -O
archive.key  
RUN apt-key add archive.key  
RUN wget
http://archive.cloudera.com/kudu/ubuntu/xenial/amd64/kudu/cloudera.list  
RUN apt-get update  
  
# Install Kudu  
RUN apt-get install -y apt-utils  
RUN apt-get -y install kudu # Base Kudu files  
RUN apt-get -y install kudu-master # Service scripts for managing kudu-master  
RUN apt-get -y install kudu-tserver # Service scripts for managing kudu-
tserver  
RUN apt-get -y install libkuduclient0 # Kudu C++ client shared library  
RUN apt-get -y install libkuduclient-dev # Kudu C++ client SDK  
  
#RUN service ntp restart  
VOLUME /var/lib/kudu/master /var/lib/kudu/tserver  
#RUN chmod -R 777 /var/lib/kudu/master  
#RUN chmod -R 777 /var/lib/kudu/tserver  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
WORKDIR /  
# 8051 for masters  
# 8050 for tablet servers  
EXPOSE 8050 8051 7050 7051  
CMD ["help"]  
  

