FROM madehao/jdk:8-centos6  
  
MAINTAINER madehao1983@sina.com  
  
# add user and group  
RUN groupadd -g 5000 tomcat && useradd -g tomcat -u 5000 tomcat -d
/home/tomcat -m  
  
# install software  
WORKDIR /usr/local  
  
RUN curl \  
http://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.30/bin/apache-
tomcat-8.5.30.tar.gz \  
-o tomcat.tar.gz \  
&& tar -zxvf tomcat.tar.gz \  
&& rm -f tomcat.tar.gz \  
&& mv apache-tomcat-* tomcat \  
&& chown -R tomcat:tomcat tomcat  
  
WORKDIR /  
  
# add env  
ENV CATALINA_HOME=/usr/local/tomcat \  
PATH=$PATH:/usr/local/tomcat/bin  
  
USER tomcat  
  
CMD ["catalina.sh","run"]  
  

