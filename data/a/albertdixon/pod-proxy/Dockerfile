FROM nginx:latest  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
ENV T2_VER=v2.2.1 \  
INIT_VER=1.0.0  
ADD
https://github.com/albertrdixon/tmplnator/releases/download/${T2_VER}/t2-linux.tgz
/t2.tgz  
ADD https://github.com/Yelp/dumb-init/releases/download/v${INIT_VER}/dumb-
init_${INIT_VER}_amd64.deb /init.deb  
ADD *.tmpl /templates/  
ADD ["entry", "start", "/sbin/"]  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends apache2-utils \  
&& dpkg -i /init.deb \  
&& chmod +rx /sbin/entry /sbin/start \  
&& tar xvzf /t2.tgz -C /bin \  
&& rm -f /t2.tgz /init.deb  
  
ENTRYPOINT ["dumb-init", "entry"]  
CMD ["start"]  
ENV LISTEN_PORT=1090 \  
UPSTREAM_HOST=127.0.0.1 \  
UPSTREAM_PORT=8080

