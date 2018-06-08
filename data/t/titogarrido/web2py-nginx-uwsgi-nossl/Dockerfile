FROM phusion/baseimage  
  
MAINTAINER Tito Garrido <titogarrido@gmail.com>  
  
# Disable ssh.. we have docker exec  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Update the system  
RUN apt-get update  
# Install NGINX  
RUN apt-get install -y \  
wget \  
vim \  
nginx-full \  
build-essential \  
python-dev \  
libxml2-dev \  
python-pip \  
unzip  
  
RUN pip install setuptools --no-use-wheel --upgrade  
# Install uwsgi  
RUN pip install --upgrade uwsgi  
  
# Configure NGINX  
RUN mkdir /etc/nginx/conf.d/web2py  
  
ADD gzip_static.conf /etc/nginx/conf.d/web2py/gzip_static.conf  
ADD gzip.conf /etc/nginx/conf.d/web2py/gzip.conf  
ADD web2py-nginx-nossl /etc/nginx/sites-available/web2py  
  
RUN ln -s /etc/nginx/sites-available/web2py /etc/nginx/sites-enabled/web2py  
RUN rm /etc/nginx/sites-enabled/default  
RUN mkdir /etc/nginx/ssl  
  
# Prepare folders for uwsgi  
RUN sudo mkdir /etc/uwsgi  
RUN sudo mkdir /var/log/uwsgi  
  
ADD web2py.ini /etc/uwsgi/web2py.ini  
  
ADD uwsgi-emperor.conf /etc/init/uwsgi-emperor.conf  
  
# Install Web2py  
RUN mkdir /home/www-data  
RUN wget http://web2py.com/examples/static/web2py_src.zip  
RUN unzip web2py_src.zip -d /home/www-data  
RUN mv /home/www-data/web2py/handlers/wsgihandler.py /home/www-
data/web2py/wsgihandler.py  
RUN rm web2py_src.zip  
RUN chown -R www-data:www-data /home/www-data/web2py  
  
# Setup nginx.conf file  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i "s/# gzip/gzip/g" /etc/nginx/nginx.conf  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /etc/service/uwsgi  
ADD uwsgi_init /etc/service/uwsgi/run  
RUN chmod 755 /etc/service/uwsgi/run  
RUN mkdir /etc/service/nginx  
ADD nginx_init /etc/service/nginx/run  
RUN chmod 755 /etc/service/nginx/run  
  
# Init script to setup web2py  
ADD web2py_setup.sh /etc/my_init.d/web2py_setup.sh  
RUN chmod 755 /etc/my_init.d/web2py_setup.sh  
  
EXPOSE 80  
WORKDIR /home/www-data/web2py  
RUN /etc/service/uwsgi/run  
RUN /etc/service/nginx/run  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

