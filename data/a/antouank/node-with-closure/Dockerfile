FROM node:slim  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get install -y git  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list.d/java-8-debian.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" >> /etc/apt/sources.list.d/java-8-debian.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
RUN apt-get update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN apt-get install -y oracle-java8-installer curl unzip  
RUN java -version  
  
COPY resources/cc.sh /opt/cc.sh  
RUN curl https://dl.google.com/closure-compiler/compiler-latest.zip >>
/tmp/cc.zip \  
&& unzip -d /tmp /tmp/cc.zip c*.jar \  
&& cp /tmp/c*.jar /opt/closure-compiler.jar \  
&& rm /tmp/c*.jar \  
&& chmod +x /opt/cc.sh  
  
CMD /opt/cc.sh  

