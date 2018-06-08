FROM centos:7  
MAINTAINER Matteo Cerutti <matteo.cerutti@hotmail.co.uk>  
  
ENV FLUFFY_VERSION 0.0.12  
RUN yum clean all && yum install -y epel-release && yum install -y python-pip
iptables gcc-c++ python-devel nc && rm -rf /var/cache/yum/* && mkdir /app &&
pip install pyfluffy==${FLUFFY_VERSION} && rm -rf /root/.cache && yum remove
-y gcc-c++  
ADD etc /etc/fluffy/  
  
VOLUME ["/var/lib/fluffy"]  
  
ENTRYPOINT ["fluffyd"]  
WORKDIR "/app"  
CMD ["--log_level", "INFO"]  

