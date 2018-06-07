FROM ubuntu:14.04  
MAINTAINER Taio Jia <jiasir@icloud.com>  
ENV REFRESHED_AT 2015-01-26  
RUN apt-get -yqq update  
RUN apt-get -yqq install wget  
VOLUME [ "/var/lib/tomcat7/webapps/" ]  
WORKDIR /var/lib/tomcat7/webapps/  
ENTRYPOINT [ "wget" ]  
CMD [ "-?" ]

