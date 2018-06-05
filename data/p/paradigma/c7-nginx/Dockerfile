FROM centos:centos7  
MAINTAINER Greco Rubio <greco@paradigma.com.mx>  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release tar ; yum clean all  
RUN yum -y install nginx ; yum clean all  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old  
ADD nginx.conf /etc/nginx/nginx.conf  
  
ADD vhost.conf /etc/nginx/conf.d/vhost.conf  
  
RUN mkdir -p /etc/service/nginx  
ADD start.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
EXPOSE 80  
ENTRYPOINT ["/etc/service/nginx/run"]  
  
CMD ["start"]  

