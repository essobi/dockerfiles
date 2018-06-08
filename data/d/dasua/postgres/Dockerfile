FROM postgres:9.6  
  
LABEL name="PostgreSQL 9.6 Docker image (Spanish - Europe/Madrid)" \  
maintainer="j.dasua@gmail.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y dist-upgrade \  
&& apt-get -y install apt-utils \  
locales \  
tzdata \  
bash-completion \  
less \  
nano \  
multitail \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb
\  
&& localedef -i es_ES -c -f UTF-8 -A /usr/share/locale/locale.alias
es_ES.UTF-8 \  
&& mkdir -p /home/postgres \  
&& chown postgres:postgres /home/postgres \  
&& true  
ENV LANG es_ES.UTF-8  
  
RUN rm /etc/localtime  
RUN echo "Europe/Madrid" > /etc/timezone && ln -s
/usr/share/zoneinfo/Europe/Madrid /etc/localtime && dpkg-reconfigure -f
noninteractive tzdata  

