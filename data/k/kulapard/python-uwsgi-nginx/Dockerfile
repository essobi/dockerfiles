FROM python:2.7-slim  
  
MAINTAINER Taras Drapalyuk <taras@drapalyuk.com>  
  
ENV NGINX_VERSION 1.10.1-1~jessie  
  
RUN set -ex \  
&& apt-key adv --keyserver hkp://pgp.mit.edu:80 \--recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
nginx=$NGINX_VERSION \  
supervisor \  
&& BUILD_DEPS='build-essential python-dev' \  
&& apt-get install -y $BUILD_DEPS --no-install-recommends \  
&& pip install --no-cache-dir \  
uwsgi \  
&& apt-get autoremove -y $BUILD_DEPS \  
&& rm -rf /usr/src/python ~/.cache \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
  
# Make NGINX run on the foreground  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
  
# Remove default configuration from Nginx  
&& rm /etc/nginx/conf.d/default.conf  
  
# Copy the modified Nginx conf  
COPY nginx.conf /etc/nginx/conf.d/  
  
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number  
COPY uwsgi.ini /etc/uwsgi/  
  
# Custom Supervisord config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY ./app /app  
WORKDIR /app  
  
EXPOSE 80  
  
CMD ["/usr/bin/supervisord", "-c/etc/supervisor/conf.d/supervisord.conf"]  

