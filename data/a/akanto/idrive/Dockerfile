FROM centos:7  
RUN yum install -y epel-release && yum clean all  
RUN yum install -y redhat-lsb supervisor wget && yum clean all  
  
ENV IDRIVE_VERSION 1.1.7  
# ADD https://www.idrive.com/ldb/downloads/idrive-datacenteredition/IDrive-
DataCenterEdition-${IDRIVE_VERSION}.tar.gz /IDrive-DataCenterEdition.tar.gz  
COPY IDrive-DataCenterEdition-${IDRIVE_VERSION}.tar.gz /IDrive-
DataCenterEdition.tar.gz  
  
RUN tar xvf /IDrive-DataCenterEdition.tar.gz \  
&& rm -f /IDrive-DataCenterEdition.tar.gz \  
&& cd IDrive-DataCenterEdition-${IDRIVE_VERSION} \  
&& ./ez_install.sh  
  
RUN export IDRIVE_USER="idrive" \  
&& export IDRIVE_UID="1100" \  
&& export IDRIVE_GROUP="idrive" \  
&& export IDRIVE_GID="1100" \  
&& export IDRIVE_PASSWORD="idrive" \  
&& groupadd ${IDRIVE_GROUP} \--gid ${IDRIVE_GID} \  
&& useradd --gid ${IDRIVE_GROUP} \--uid ${IDRIVE_UID} ${IDRIVE_USER} \  
&& echo ${IDRIVE_PASSWORD} | passwd ${IDRIVE_USER} \--stdin \  
&& mkdir /home/idrive/.idrive && chown ${IDRIVE_USER}:${IDRIVE_GROUP}
/home/idrive/.idrive  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME ["/etc/idrive", "/home/idrive/.idrive", "/data"]  
  
EXPOSE 5001  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

