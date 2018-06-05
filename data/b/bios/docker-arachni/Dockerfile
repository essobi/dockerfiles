# arachni  
FROM centos:centos7  
MAINTAINER Tobias Sgoff  
  
ENV
src="https://github.com/Arachni/arachni/releases/download/v1.5.1/arachni-1.5.1-0.5.12-linux-x86_64.tar.gz"  
ENV PATH=${PATH}:/data/arachni/bin  
  
RUN yum -y install tar && mkdir /data && cd $_ && curl $src -Lo arachni.tar.gz
&& /usr/bin/tar xzf arachni.tar.gz \  
&& rm -f ./*.gz && mv ara* arachni  
  
WORKDIR /data/arachni/bin  

