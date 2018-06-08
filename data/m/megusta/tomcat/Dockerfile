FROM ubuntu:14.04  
MAINTAINER Christoph <christoph@megusta.ag>  
ENV CREATED_AT 15-01-03  
# PORTS  
EXPOSE 8080 7777  
# ON DERIVED IMAGES  
ONBUILD EXPOSE 8080 7777  
ONBUILD RUN rm -rf /home/mega/tomcat/webapps && mkdir -p
/home/mega/tomcat/webapps  
ONBUILD COPY *.war /home/mega/tomcat/webapps/  
ONBUILD USER root  
ONBUILD RUN chown -R mega:mega /home/mega  
ONBUILD WORKDIR /home/mega/tomcat  
ONBUILD USER mega  
ONBUILD ENV HOME /home/mega  
# ENTRY  
ENTRYPOINT ["/home/mega/tomcat/run.sh"]  
  
# -----------------  
# ROOT INSTALLATION  
# -----------------  
# Install packages  
# General system update and tools  
# - Tools  
# - Install Oracle Java 7 JDK  
# and then  
# Add less-privileged user "mega" with same password  
# and add sudo privilege without password  
RUN apt-get update -qq && \  
apt-get upgrade -qqy && \  
apt-get install --no-install-recommends git-core zip unzip wget curl software-
properties-common pwgen ca-certificates nano screen nginx apache2-utils -qqy
&& \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update -qq && \  
$(echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections) && \  
apt-get install oracle-java7-installer -qqy && \  
apt-get install oracle-java7-set-default -qqy && \  
apt-get clean -qqy && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
adduser mega --home /home/mega --gecos "" \--disabled-password && \  
$(echo "mega:mega" | chpasswd) && \  
usermod -a -G sudo mega && \  
bash -c "echo 'mega ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers"  
  
# -----------------------  
# USER-SPACE INSTALLATION  
# -----------------------  
# Login as user  
USER mega  
ENV HOME /home/mega  
WORKDIR /home/mega  
  
ENV TOMCAT_MAJOR_VERSION 7  
ENV TOMCAT_MINOR_VERSION 7.0.57  
ENV CATALINA_HOME /home/mega/tomcat  
  
# INSTALL TOMCAT  
# and remove useless webapps like ROOT, docs and examples  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* tomcat && \  
rm -rf tomcat/webapps/ROOT && rm -rf tomcat/webapps/examples && rm -rf
tomcat/webapps/docs  
# make tomcat dir as workdir  
WORKDIR /home/mega/tomcat  
  
ADD create_tomcat_admin_user.sh /home/mega/tomcat/create_tomcat_admin_user.sh  
ADD run.sh /home/mega/tomcat/run.sh  
USER root  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD setenv.sh /home/mega/tomcat/bin/setenv.sh  
ADD appenv.sh /home/mega/tomcat/bin/appenv.sh  
RUN chown -R mega:mega /home/mega  
USER mega  

