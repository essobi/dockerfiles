FROM centos:latest  
  
ENV WAPITI_VERSION 2.3.0  
ENV LANG en_US  
ENV PATH /opt/wapiti/bin:$PATH  
  
RUN yum -y update \  
&& yum -y install epel-release \  
&& yum -y install wget python-requests python-beautifulsoup openssl \  
&& yum clean all \  
&& mkdir -p /opt \  
&& cd /opt \  
&& wget
http://downloads.sourceforge.net/project/wapiti/wapiti/wapiti-${WAPITI_VERSION}/wapiti-${WAPITI_VERSION}.tar.gz
\  
&& tar xfvz wapiti-${WAPITI_VERSION}.tar.gz \  
&& rm -fr wapiti-${WAPITI_VERSION}.tar.gz \  
&& cd wapiti-${WAPITI_VERSION} \  
&& ln -sF /opt/wapiti-${WAPITI_VERSION} /opt/wapiti \  
&& chmod 755 /opt/wapiti/bin/wapiti \  
&& adduser -d /workdir -s /bin/bash wapiti  
  
USER wapiti  
  
VOLUME /workdir  
WORKDIR /workdir  
  
ENTRYPOINT ["wapiti"]  
  
CMD ["--help"]  

