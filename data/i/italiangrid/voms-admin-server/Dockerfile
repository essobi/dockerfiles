FROM italiangrid/base-dev:latest  
  
RUN sed -i 's/socket_timeout=3/socket_timeout=1/'
/etc/yum/pluginconf.d/fastestmirror.conf && \  
echo "include_only=.garr.it,.cern.ch" >>
/etc/yum/pluginconf.d/fastestmirror.conf && \  
mkdir /scripts  
  
ADD setup /scripts  
  
RUN yum -y install sudo && sh /scripts/setup-voms-user.sh  
  
RUN chmod 755 "/scripts/run.sh"  
RUN cp /scripts/emi-oracle-11.repo /etc/yum.repos.d && \  
yum -y -d2 install oracle-instantclient-basic \  
java-1.6.0-openjdk-devel \  
java-1.8.0-openjdk-devel \  
voms-admin-client \  
voms-admin-server  
  
ENV VOMS_DB_USERNAME voms  
ENV VOMS_DB_PASSWORD pwd  
ENV VOMS_DB_NAME voms_test  
ENV VOMS_MAIL_FROM voms-admin@dev.local.io  
ENV VOMS_HOSTNAME dev.local.io  
  
VOLUME /var/log/voms-admin  
CMD /scripts/run.sh  
  
EXPOSE 8443 1044  

