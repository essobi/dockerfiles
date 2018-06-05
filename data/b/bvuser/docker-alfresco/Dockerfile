FROM centos:centos7  
MAINTAINER Pincemail Sebastien <pincemail.sebastien@gmail.com>  
  
####SSH CONFIG  
RUN yum update -y  
RUN yum install -y openssh-server which  
RUN mkdir -p /var/run/sshd && \  
echo "root:changeme" | chpasswd  
ADD init-functions /etc/rc.d/init.d/functions  
RUN /usr/sbin/sshd-keygen  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
# install some necessary/desired RPMs and get updates  
RUN yum update -y  
RUN yum install -y chkconfig && \  
yum install -y unzip && \  
yum install -y wget  
  
RUN mkdir -p /appli/alfresco  
  
# install java  
COPY assets/install_java.sh /tmp/install_java.sh  
RUN chmod 755 /tmp/install_java.sh  
RUN /tmp/install_java.sh  
  
# install alfresco  
COPY assets/install_alfresco.sh /tmp/install_alfresco.sh  
RUN chmod 755 /tmp/install_alfresco.sh  
RUN /tmp/install_alfresco.sh  
RUN mkdir -p /appli/alfresco/alf_data  
COPY assets/keystore /appli/keystore  
  
# this is for LDAP configuration  
RUN mkdir -p
/appli/alfresco/tomcat/shared/classes/alfresco/extension/subsystems/Authentication/ldap/ldap1/  
COPY assets/ldap-authentication.properties
/appli/alfresco/tomcat/shared/classes/alfresco/extension/subsystems/Authentication/ldap/ldap1/ldap-
authentication.properties  
RUN mkdir -p /appli/alfresco/application/logs  
COPY assets/init.sh /appli/alfresco/init.sh  
  
# Alfresco configuration  
COPY assets/properties.ini /appli/alfresco/properties.ini  
COPY assets/alfresco-global.properties
/appli/alfresco/tomcat/shared/classes/alfresco-global.properties  
  
RUN chmod 755 /appli/alfresco/init.sh  
RUN useradd -d /home/tomcat -m tomcat && mkdir -p /home/tomcat/.ssh  
RUN chown -R tomcat:tomcat /home/tomcat  
RUN mkdir -p /etc/sudoers.d  
RUN echo "tomcat ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-cloud-init-users  
RUN chown -R tomcat:tomcat /appli  
RUN yum clean all  
RUN yum install passwd -y  
  
EXPOSE 22 21 137 138 139 445 7070 8080  
WORKDIR /alfresco  
  
# install supervisor  
COPY assets/install_supervisor.sh /tmp/install_supervisor.sh  
RUN /tmp/install_supervisor.sh  
RUN mkdir -p /appli/supervisor  
RUN chmod 777 /appli/supervisor  
COPY assets/supervisord.conf /etc/supervisord.conf  
CMD /usr/bin/supervisord -c /etc/supervisord.conf -n  

