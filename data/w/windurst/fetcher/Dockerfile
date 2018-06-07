FROM ubuntu:14.04  
MAINTAINER Douglas Rae "rae.doug@gmail.com"  
ENV REFRESHED_AT 2015-02-05  
#RUN apt-get -y update  
RUN apt-get -yqq install wget  
  
VOLUME [ "/var/lib/tomcat7/webapps/" ]  
WORKDIR /var/lib/tomcat7/webapps/  
  
ENTRYPOINT [ "wget" ]  
CMD [ "-?" ]  

