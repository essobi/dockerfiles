from ubuntu:xenial  
  
#set the locale  
RUN apt-get -qq update && \  
apt-get -q -y upgrade && \  
apt-get install -y sudo curl wget locales && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update  
# make sure that locales package is available  
RUN apt-get install --reinstall -y locales  
# uncomment chosen locale to enable it's generation  
RUN sed -i 's/ de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen  
# generate chosen locale  
RUN locale-gen de_DE.UTF-8  
# set system-wide locale settings  
ENV LANG de_DE.UTF-8  
ENV LANGUAGE de_DE:de  
ENV LC_ALL de_DE.UTF-8  
# verify modified configuration  
#WORKDIR /etc/default/locale  
#COPY etc/default/locale /etc/default/locale  
#RUN chmod 0755 /etc/default/locale  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
  
ENV TOMCAT_VERSION 8.0.52  
# Install dependencies  
RUN apt-get update && apt-get install -y git build-essential curl wget
software-properties-common  
  
# Install JDK 8  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer wget unzip tar && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get install -y oracle-java8-set-default  
  
# Get Tomcat  
RUN wget --quiet --no-cookies
http://apache.rediris.es/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \  
tar xzvf /tmp/tomcat.tgz -C /usr/local && \  
mv /usr/local/apache-tomcat-${TOMCAT_VERSION}/* /usr/local/tomcat/ && \  
rm /tmp/tomcat.tgz && \  
rm -rf /usr/local/tomcat/webapps/examples && \  
rm -rf /usr/local/tomcat/webapps/docs && \  
rm -rf /usr/local/tomcat/webapps/ROOT  
  
WORKDIR $CATALINA_HOME  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  
  

