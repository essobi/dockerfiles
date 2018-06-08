FROM centos:7  
MAINTAINER Luca Pasquale  
  
ENV TORQUE_VERSION=6.0.2  
RUN yum -y install libtool openssl-devel libxml2-devel boost-devel gcc gcc-c++
wget  
RUN wget http://www.adaptivecomputing.com/index.php?wpfb_dl=3124 -O
torque-${TORQUE_VERSION}.tar.gz  
RUN tar -xf torque-${TORQUE_VERSION}.tar.gz && rm
torque-${TORQUE_VERSION}.tar.gz  
RUN yum -y group install "Development Tools"  
RUN cd $(ls -d torque*)/ && \  
./configure && \  
make && \  
make install  
  
RUN yum -y install nfs-utils openldap-clients nss-pam-ldapd authconfig  
  
COPY init.sh /init.sh  
RUN chmod u+x /init.sh  
  
ENV PBS_HOME=/var/spool/torque  
  
EXPOSE 15002  
EXPOSE 15003  
CMD /init.sh  

