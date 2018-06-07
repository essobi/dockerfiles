FROM java:8  
MAINTAINER rkumari@nulli.com  
  
WORKDIR /opt  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
  
# Path to secret file that contains the cn=Directory Manager password  
# Used to configure the image  
# Mount a docker volume or K8S secret volume on /var/secrets/opendj  
# This is the path to the password file  
# If no volume is mounted, a default password is set  
ENV DIR_MANAGER_PW_FILE /var/secrets/opendj/dirmanager.pw  
  
ENV OPENDJ_VERSION=3.5.1  
COPY bootstrap/ldif/cts-add-schema.ldif /tmp/cts-add-schema.ldif  
COPY bootstrap/ldif/cts_acis.ldif /tmp/cts_acis.ldif  
COPY bootstrap/ldif/cts-indices.ldif /tmp/cts-indices.ldif  
COPY bootstrap/ldif/cts-container.ldif /tmp/cts-container.ldif  
COPY bootstrap/ldif/cts_user.ldif /tmp/cts_user.ldif  
  
COPY opendj/opendj-$OPENDJ_VERSION.zip /tmp/opendj.zip  
RUN unzip /tmp/opendj.zip -d /opt \  
&& rm /tmp/*zip  
  
# When testing the build it is faster to use local files  
#ADD opendj.zip /tmp/  
#RUN unzip /tmp/opendj.zip -d /opt  
RUN apt-get update  
RUN apt-get install -y vim net-tools telnet  
  
WORKDIR /opt/opendj  
  
# Creating instance.loc consolidates the writable directories under one root  
# We also create the extensions directory  
# We set a dir manager default password value here, but this is almost  
# certainly not what you want. This hard coded path to the password  
# should get over mounted by a secret volume with the "real" password. See the
README  
RUN echo "/opt/opendj/data" > /opt/opendj/instance.loc && \  
mkdir -p /opt/opendj/data/lib/extensions && \  
mkdir -p /var/secrets/opendj && \  
echo "password" > ${DIR_MANAGER_PW_FILE}  
  
ADD Dockerfile /  
  
ADD bootstrap/ /opt/opendj/bootstrap/  
  
# OpenDJ Dictionary Password Policy: forbidden words in pwds  
COPY dict.txt /opt/opendj/dict.txt  
  
EXPOSE 389 636 4444 8989  
ADD run.sh /opt/opendj/run.sh  
  
CMD ["/opt/opendj/run.sh"]  

