FROM ubuntu:15.10  
MAINTAINER Plamen Tanov "ptanov@setelis.com"  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y apache2  
  
RUN mkdir /etc/apache2/conf.d  
  
RUN apt-get install -y w3c-markup-validator libapache2-mod-perl2 openjdk-8-jdk
git mercurial subversion python unzip supervisor  
  
ADD ./resources/serve-cgi-bin.conf /etc/apache2/conf-available/serve-cgi-
bin.conf  
ADD ./resources/supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN sed 's/Allow Private IPs = no/Allow Private IPs = yes/' -i
/etc/w3c/validator.conf  
RUN sed 's/#HTML5/HTML5/' -i /etc/w3c/validator.conf  
  
ADD
https://github.com/validator/validator/releases/download/15.6.29/vnu.jar_15.6.29.zip
/root/build/  
RUN unzip -j /root/build/vnu*.zip -d /root/build/validator.nu  
  
RUN apt-get clean  
  
EXPOSE 80  
EXPOSE 8888  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  
  

