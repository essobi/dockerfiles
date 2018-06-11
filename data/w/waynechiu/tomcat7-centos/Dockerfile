# This dockerfile uses the Centos image with tomcat-7.0  
# VERSION 1 - EDITION 1  
# Author: Wayne Chiu  
# Command format: Instruction [arguments / command] ..  
FROM centos:6.6  
MAINTAINER Wayne Chiu hjk25323100@gmail.com  
  
# Setting Envirnoment  
ENV CATALINA_HOME /usr/local/tomcat  
ENV JAVA_HOME /usr/local/jdk1.7.0_55  
ENV PATH $CATALINA_HOME/bin:$JAVA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# Install Supervisor  
RUN yum -y update \  
&& yum install -y python-setuptools openssh* tar wget\  
&& easy_install supervisor  
  
# Install Java  
RUN wget --no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.tar.gz" \  
-O jdk-7-linux-x64.tar.gz \  
&& tar zxvf jdk-7-linux-x64.tar.gz \  
&& mv jdk1.7.0_55 /usr/local \  
&& rm -rf jdk-7-linux-x64.tar.gz  
RUN mkdir -p /var/run/sshd && \  
mkdir -p /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisord.conf  
  
#SSH authorized_keys  
ADD authorized_keys /root/.ssh/authorized_keys  
RUN chmod 600 /root/.ssh/authorized_keys  
#  
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
  
# Volume  
VOLUME ["/usr/local/tomcat/webapps/ROOT"]  
  
# Setting tomcat port  
EXPOSE 8080 22 80  
CMD ["/usr/bin/supervisord"]  

