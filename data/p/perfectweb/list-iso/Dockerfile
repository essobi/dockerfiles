FROM nginx  
MAINTAINER Alin Jurj <office@perfectweb.ro>  
  
ENV ISO http://cloud.centos.org/centos/7/atomic/images/CentOS-Atomic-
Host-7-Installer.iso  
  
WORKDIR /usr/share/nginx/html/  
  
RUN apt-get update  
RUN apt-get install -y wget bsdtar  
RUN rm -rf *  
  
RUN sed -i.bak "s/location \/ {/location \/ { autoindex on;/g"
/etc/nginx/conf.d/default.conf  
  
WORKDIR /root/  
ADD . run.sh  
  
CMD ["/root/run.sh"]  

