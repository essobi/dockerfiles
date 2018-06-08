FROM python:3.5  
MAINTAINER Nazim Lala <naziml@microsoft.com>  
  
ENV NGINX_VERSION 1.12.0-1~jessie  
  
# Setup webserver and process manager  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
gettext-base \  
supervisor \  
openssh-server \  
dos2unix \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& rm /etc/nginx/conf.d/default.conf \  
&& echo "root:Docker!" | chpasswd  
  
COPY nginx.conf /etc/nginx/conf.d/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY sshd_config /etc/ssh/  
COPY init_container.sh /bin/  
COPY uwsgi.ini /etc/uwsgi/  
  
# Install uwsgi  
RUN pip install uwsgi \  
&& dos2unix /bin/init_container.sh \  
&& dos2unix /etc/ssh/sshd_config \  
&& dos2unix /etc/uwsgi/uwsgi.ini \  
&& chmod 755 /bin/init_container.sh  
  
# Install flask  
RUN pip install flask  
  
# Copy app  
COPY ./app /app  
WORKDIR /app  
  
EXPOSE 80 2222  
CMD ["/bin/init_container.sh"]  

