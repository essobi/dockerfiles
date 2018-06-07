FROM ubuntu:14.04  
MAINTAINER Axel Oehmichen <axelfrancois.oehmichen11@imperial.ac.uk>  
  
WORKDIR /root  
  
ADD start_eae.sh /root  
  
## We install all the dependencies  
RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \  
&& apt-get install -y wget curl git unzip zip tomcat7 libncurses-dev psmisc
default-jdk vim htop openssh-server \  
&& apt-get install -y tcl-dev  
  
## We install openlava  
RUN curl -L https://github.com/aoehmichen/eae-files/raw/master/op.tar.gz -o
/root/op.tar.gz \  
&& tar zxvf /root/op.tar.gz openlava-3.3 \  
&& cd openlava-3.* \  
&& ./configure \  
&& make \  
&& make install \  
&& cd config \  
&& cp lsb.params lsb.users lsf.conf lsf.shared lsf.task openlava.*
/opt/openlava-3.3/etc/ \  
&& useradd -r openlava \  
&& chown -R openlava:openlava /opt/openlava-3.*/ \  
&& cp /opt/openlava-3.*/etc/openlava /etc/init.d \  
&& update-rc.d openlava defaults \  
&& cp /opt/openlava-3.3/etc/openlava.* /etc/profile.d \  
&& chown openlava:openlava /etc/profile.d/openlava.* \  
&& chmod 755 /etc/profile.d/openlava.sh  
  
# We set the configuration files  
RUN curl -L https://github.com/aoehmichen/eae-
files/raw/master/interfaceEAE.war -o /var/lib/tomcat7/webapps/interfaceEAE.war
\  
&& chown openlava:openlava /opt/openlava-3.3/etc/*  
  
# We create the eae user and set the tomcat to run as the newly created eae
user  
RUN useradd -ms /bin/bash eae \  
&& mkdir -p /home/eae/.grails/interfaceEAEConfig \  
&& chown -R eae:eae /home/eae/.grails/ \  
&& sed -i "s/TOMCAT7_USER=tomcat7/TOMCAT7_USER=eae/g" /etc/default/tomcat7 \  
&& sed -i "s/TOMCAT7_GROUP=tomcat7/TOMCAT7_GROUP=eae/g" /etc/default/tomcat7 \  
&& /usr/lib/jvm/default-java/bin/keytool -genkey -alias tomcat -keyalg RSA
-storepass changeit -keypass changeit -validity 365 -dname "cn=AOehmichen,
ou=eAE, o=DSI, c=UK" \  
&& mv /root/.keystore /home/eae/ \  
&& chown eae:eae /home/eae/.keystore \  
&& sed -i -e '87d;91d' /var/lib/tomcat7/conf/server.xml \  
&& sed -i "s/sslProtocol=\"TLS\"/sslProtocol=\"TLS\"
keystorePass=\"changeit\"/g" /var/lib/tomcat7/conf/server.xml \  
&& chown -R eae:eae /var/log/tomcat7 \  
&& chmod 777 /var/lib/tomcat7/logs \  
&& chown eae:eae /var/lib/tomcat7/webapps \  
&& chown eae:eae /var/cache/tomcat7 \  
&& chown -R root:eae /var/lib/tomcat7/conf/ \  
&& rm -rf /var/log/tomcat7/* \  
&& usermod -a -G tomcat7 eae  
  
# We set up the ssh keys for user eae  
USER eae  
WORKDIR /home/eae  
RUN mkdir ~/.ssh && chmod 700 ~/.ssh \  
&& mkdir -p data \  
&& chmod 777 data \  
&& git clone -b unsecure https://github.com/aoehmichen/AnalyticsEAE.git
/home/eae/AnalyticsEAE \  
&& curl -L
"https://raw.githubusercontent.com/aoehmichen/interfaceEAE/master/web-
app/Scripts/putToHDFS.sh" > putToHDFS.sh \  
&& chmod +x putToHDFS.sh  
  
USER root  
RUN echo "Host *" > /home/eae/.ssh/config \  
&& echo " StrictHostKeyChecking no" >> /home/eae/.ssh/config \  
&& chown -R eae:eae .ssh/  
  
EXPOSE 22 8443 16322 16323 16324 16325  
EXPOSE 16322/udp  
  
ENTRYPOINT ["bash", "/root/start_eae.sh"]  
  
CMD ["-bash", "Unsecure"]  

