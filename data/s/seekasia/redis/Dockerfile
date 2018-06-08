FROM redis:3.2.3  
MAINTAINER "Sook Teng" <sookteng.looi@seekasia.com>  
  
ENV TZ Asia/Singapore  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y --no-install-recommends install logrotate \  
&& apt-get -y --no-install-recommends install ruby2.1 \  
&& gem2.1 install redis -v 3.3.1 \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD src/redis-trib-pass.rb /usr/local/bin/redis-trib-pass.rb  
RUN chmod +x /usr/local/bin/redis-trib-pass.rb  
  
COPY docker-entrypoint-all.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint-all.sh  
ENTRYPOINT ["docker-entrypoint-all.sh"]  

