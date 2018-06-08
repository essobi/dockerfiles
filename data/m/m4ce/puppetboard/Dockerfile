FROM centos:7  
MAINTAINER Matteo Cerutti <matteo.cerutti@hotmail.co.uk>  
  
ENV PUPPETBOARD_VERSION "0.2.0"  
RUN yum clean all && yum install -y epel-release && yum install -y python-pip
supervisor nginx uwsgi uwsgi-plugin-python && rm -rf /var/cache/yum/* && pip
install puppetboard==$PUPPETBOARD_VERSION && rm -rf /root/.cache  
  
COPY files/supervisor.ini /etc/supervisord.d/puppetboard.ini  
COPY files/settings.py /etc/puppetboard/  
COPY files/wsgi.py /app/  
COPY files/wsgi.ini /app/  
COPY files/nginx.conf /etc/nginx/  
  
EXPOSE 8000  
WORKDIR /app  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

