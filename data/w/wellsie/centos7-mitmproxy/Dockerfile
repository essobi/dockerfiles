FROM wellsie/centos7-python  
MAINTAINER Jono Wells <_oj.io>  
  
RUN yum install -y \  
libffi-devel \  
libxml2-devel \  
libxslt-devel \  
openssl-devel ;\  
yum -y clean all ;\  
pip install mitmproxy ;\  
mkdir /mitmproxy  
  
VOLUME /mitmproxy  
WORKDIR /mitmproxy  
  
ENV LANG en_US.UTF-8  
EXPOSE 8080  
CMD [ "mitmproxy" ]  

