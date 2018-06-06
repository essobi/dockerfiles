FROM debian:latest  
MAINTAINER "Fang Yunlin"  
  
RUN apt-get update \  
&& apt-get install -y wget unzip supervisor \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# download jdk8  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz -O
/tmp/jdk-8u66-linux-x64.tar.gz \  
&& tar xzvf /tmp/jdk-8u66-linux-x64.tar.gz -C /var/lib/ \  
&& rm -f /tmp/jdk-8u66-linux-x64.tar.gz  
  
# download glassfish 4.1.1  
  
RUN wget http://download.java.net/glassfish/4.1.1/release/glassfish-4.1.1.zip
-O /tmp/glassfish-4.1.1.zip \  
&& unzip -o -d /var/lib/ /tmp/glassfish-4.1.1.zip \  
&& rm -f /tmp/glassfish-4.1.1.zip  
  
# environment variables  
ENV JAVA_HOME /var/lib/jdk1.8.0_66  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# start up glassfish  
ADD glassfish.conf /etc/supervisor/conf.d  
  
EXPOSE 8080 4848  
CMD ["/usr/bin/supervisord", "-n"]  

