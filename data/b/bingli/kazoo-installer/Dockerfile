FROM bingli/kazoo-base  
MAINTAINER Bing Li <enst.bupt@gmail.com>  
  
RUN yum update -y && yum install -y git  
  
#in order to build kazoo  
#RUN yum install -y nc libxslt zip unzip gcc libstdc++-devel libxml2-devel
expat-devel  
WORKDIR /tmp/  
RUN git clone https://github.com/2600hz/community-scripts.git  
RUN cp -r community-scripts/simple-installer /opt/kazoo_install  
RUN rm -rf commumity-scripts  
  
ADD number_manager.py /root/  
  
#iptables may cause exit  
RUN sed -i '/iptables/s/^/#/' /opt/kazoo_install/setup_packages  
  
WORKDIR /opt/kazoo_install  
  
RUN chmod +x setup* install*  
  
CMD ./install_kazoo  
  

