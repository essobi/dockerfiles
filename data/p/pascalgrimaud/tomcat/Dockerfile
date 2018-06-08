FROM pascalgrimaud/ubuntu  
MAINTAINER Pascal Grimaud <pascalgrimaud@gmail.com>  
  
# update  
RUN apt-get -y update  
  
# install utilities  
RUN apt-get -y install wget  
  
# install java7  
RUN apt-get install -y openjdk-7-jre  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
# install tomcat  
RUN wget -O /tmp/apache-tomcat-8.0.23.tar.gz \  
http://apache.mirrors.ovh.net/ftp.apache.org/dist/tomcat/tomcat-8/v8.0.23/bin/apache-
tomcat-8.0.23.tar.gz  
RUN echo "f4381824abf458650f72ec12d8e81fde /tmp/apache-tomcat-8.0.23.tar.gz" |
md5sum -c  
RUN tar zxvf /tmp/apache-tomcat-8.0.23.tar.gz -C /opt/  
ENV CATALINA_HOME /opt/apache-tomcat-8.0.23  
# clean  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# expose ports  
EXPOSE 8080  
# add help  
ADD help help.txt /  
RUN chmod 755 /help  
  
# script to start the container  
ADD tomcat_run.sh /tomcat_run.sh  
RUN chmod 755 /*.sh  
CMD ["/tomcat_run.sh"]  

