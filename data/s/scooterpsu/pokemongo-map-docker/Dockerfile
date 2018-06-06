FROM frolvlad/alpine-glibc  
MAINTAINER scooterpsu <scooterpsu@gmail.com>  
  
ENV TAG develop  
EXPOSE 5000  
STOPSIGNAL SIGINT  
  
RUN apk --update add --virtual build-dependencies \  
build-base \  
nodejs \  
git \  
py-pip \  
&& apk --update add --virtual app-dependencies \  
ca-certificates \  
python-dev \  
supervisor \  
bash \  
openssh  
  
RUN git clone -b $TAG https://github.com/PokemonGoMap/PokemonGo-Map.git /app  
  
RUN pip install --no-cache-dir -r /app/requirements.txt  
  
RUN cd /app \  
&& npm install \  
&& npm run build \  
&& rm -rf node_modules \  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
RUN mv /app/config/config.ini.example /tmp/config.ini.example  
  
VOLUME ["/app/config"]  
  
COPY run.sh /run.sh  
COPY supervisord.conf /etc/supervisord/supervisord.conf  
COPY ping.html /app/static/ping.html  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord/supervisord.conf"]  

