# This dockerfile uses the Centos image with tomcat-7.0  
# VERSION 1 - EDITION 1  
# Author: Wayne Chiu  
# Command format: Instruction [arguments / command] ..  
FROM java:7-jre  
  
MAINTAINER Wayne Chiu hjk25323100@gmail.com  
  
  
  
# Setting Envirnoment  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# Set SSL key  
RUN gpg --keyserver pgpkeys.mit.edu --recv-key 40976EAF437D05B5  
RUN gpg -a --export 40976EAF437D05B5 | apt-key add -  
  
# Install Supervisor  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y apache2 supervisor openssh-server  
  
RUN mkdir -p /var/run/sshd && \  
mkdir -p /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# SSH authorized_keys  
# should create authorized in local  
ADD authorized_keys /root/.ssh/authorized_keys  
RUN chmod 600 /root/.ssh/authorized_keys  
  
# Tomcat7 Key  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \  
05AB33110949707C93A279E3D3EFE6B686867BA6 \  
07E48665A34DCAFAE522E5E6266191C37C037D42 \  
47309207D818FFD8DCD3F83F1931D684307A10A5 \  
541FBE7D8F78B25E055DDEE13C370389288584E7 \  
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
713DA88BE50911535FE716F5208B0AB1D63011C7 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
9BA44C2621385CB966EBA586F72C284D731FABEE \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
  
# Download tomcat7 server and remove file  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.63  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --verify tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
RUN chmod -R 777 /usr/local/tomcat  
  
# Setting tomcat port  
EXPOSE 8080 22 80  
# Volume  
VOLUME ["/usr/local/tomcat/webapps/ROOT"]  
  
CMD ["/usr/bin/supervisord"]  

