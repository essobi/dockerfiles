FROM python:3.4-slim  
MAINTAINER Mario César Señoranis Ayala <mariocesar.c50@gmail.com>  
  
ENV TERM xterm-256color  
ENV DEBIAN_FRONTEND noninteractive  
ENV PYTHONBUFFERED 1  
RUN apt-get update -y \  
&& apt-get install --no-install-recommends -y -q \  
libmemcached-dev postgresql-client libpq-dev \  
libpng-dev libfreetype6-dev libjpeg-dev \  
make gcc libjansson-dev libpcre3 libpcre3-dev libssl-dev \  
git \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN pip install pip==7.0.3 uwsgi==2.0.1 wheel==0.24.0  
RUN rm -rf /root/.cache  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
WORKDIR /app  
VOLUME ["/app/src", "/app/tests", "/app/public", "/app/var"]  
  
ONBUILD ENV XDG_CACHE_HOME /app/var  
ONBUILD ADD uwsgi.ini /app/uwsgi.ini  
ONBUILD ADD mime.types /app/mime.types  
ONBUILD ADD requirements.txt /app/requirements.txt  
ONBUILD ADD MANIFEST.in /app/MANIFEST.in  
ONBUILD ADD setup.cfg /app/setup.cfg  
ONBUILD ADD setup.py /app/setup.py  
  
EXPOSE 8000  
ENTRYPOINT ["/entrypoint.sh"]  
CMD []  

