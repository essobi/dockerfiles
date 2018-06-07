FROM phusion/passenger-customizable:0.9.32  
MAINTAINER Sergio Abramchuk <ss.abramchuk@gmail.com>  
  
ENV HOME=/root \  
DEBIAN_FRONTEND=noninteractive \  
TAIGA_VERSION=3.3.3-stable  
  
# Install dependencies  
RUN sed -i '/minimal_apt_get_install/s/python3/python3 python3-pip
python3-setuptools python3-wheel/' /pd_build/python.sh  
RUN /pd_build/python.sh && \  
ln -s $(command -v python3) /usr/local/bin/python && \  
ln -s $(command -v pip3) /usr/local/bin/pip && \  
pip install envtpl  
  
# Install Taiga frontend  
RUN mkdir -p /home/app/taiga /home/app/taiga/media /home/app/taiga/static && \  
git clone https://github.com/taigaio/taiga-front-dist.git
/home/app/taiga/frontend && \  
cd /home/app/taiga/frontend && git checkout $TAIGA_VERSION  
  
# Clean APT  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configuration  
RUN rm -f /etc/service/nginx/down  
RUN mkdir -p /home/app/taiga/conf-template /etc/nginx/certs && \  
sed -i '/passenger.conf/s/include/# include/' /etc/nginx/nginx.conf && \  
rm -f /etc/nginx/sites-enabled/default  
COPY ./conf/vhost.conf.j2 /home/app/taiga/conf-template/vhost.conf.j2  
COPY ./conf/frontend.conf.j2 /home/app/taiga/conf-template/frontend.conf.j2  
COPY ./conf/proxy-map.conf /etc/nginx/conf.d/proxy-map.conf  
COPY ./scripts/configure.sh /etc/my_init.d/configure.sh  
RUN chmod +x /etc/my_init.d/configure.sh  
  
# Workaround for missing group name specified in the logrotate configuration  
RUN sed -i '/su root syslog/s/syslog/adm/' /etc/logrotate.conf  
  
EXPOSE 80 443  
CMD ["/sbin/my_init"]  

