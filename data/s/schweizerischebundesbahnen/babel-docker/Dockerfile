FROM centos:7  
#  
#
https://wiki.eclipse.org/Babel_/_Server_Tool_Development_Process#Setting_up_a_Development_Environment  
#  
EXPOSE 80  
# install basic tools  
RUN yum install -y php php-mysql httpd git java-1.8.0 \  
&& yum clean all  
  
#Edit (eg) /etc/php.ini  
# short_open_tag = On  
RUN sed -ie 's/short_open_tag = Off/short_open_tag = On /g' /etc/php.ini  
  
# get code  
# git clone git://git.eclipse.org/gitroot/babel/server.git  
RUN git clone https://github.com/SchweizerischeBundesbahnen/babel-docker.git
/var/www/babel  
  
# configure apache  
ADD config/babel.conf /etc/httpd/conf.d/  
RUN rm -f /etc/httpd/conf.d/welcome.conf  
  
CMD [ "httpd", "-D FOREGROUND" ]  

