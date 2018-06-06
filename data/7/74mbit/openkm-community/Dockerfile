FROM ubuntu:16.04  
MAINTAINER Matthias Bittner <74mbit+dockerhub@gmail.com>  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV TOMCAT_VERSION 7.0.54  
ENV JAVA_HOME /usr/local/java  
ENV ORACLE_JAVA_HOME /usr/lib/jvm/java-8-oracle/  
ENV TERM xterm  
ENV OPENKM_VERSION 6.3.2  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y python-software-properties software-properties-common \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer libreoffice imagemagick swftools
liblog4j1.2-java libgnumail-java ant wget curl unzip sudo tar  
  
RUN set -xe \  
&& ln -s $ORACLE_JAVA_HOME $JAVA_HOME  
  
RUN set -xe \  
&& wget
"https://sourceforge.net/projects/openkm/files/$OPENKM_VERSION/openkm-$OPENKM_VERSION-
community-tomcat-bundle.zip/download" -O /usr/local/openkm-tomcat-bundle.zip  
  
RUN set -xe \  
&& unzip /usr/local/openkm-tomcat-bundle.zip -d /usr/local/ \  
&& rm /usr/local/openkm-tomcat-bundle.zip \  
&& ln -s $CATALINA_HOME /opt/openkm  
  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
COPY ./conf/OpenKM.cfg /usr/local/tomcat/OpenKM.cfg  
COPY ./conf/OpenKM.xml /usr/local/tomcat/OpenKM.xml  
COPY ./conf/server.xml /usr/local/tomcat/conf/server.xml  
  
RUN set -xe \  
&& apt-get -y clean  
  
VOLUME ["/data"]  
EXPOSE 8080 2002  
CMD /opt/openkm/bin/catalina.sh run  

