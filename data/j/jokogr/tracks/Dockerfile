FROM ubuntu:xenial  
MAINTAINER Ioannis Koutras <ioannis.koutras@gmail.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y wget ruby bundler \  
zlib1g-dev sqlite3 libsqlite3-dev nginx supervisor git \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm /etc/nginx/sites-enabled/default  
  
RUN wget https://github.com/TracksApp/tracks/archive/master.tar.gz \  
&& mkdir /usr/local/share/tracks \  
&& tar xzf master.tar.gz --strip-components=1 -C \  
/usr/local/share/tracks \  
&& rm master.tar.gz  
  
# Add puma gem, remove mysql2 gem and install all the gems  
RUN cd /usr/local/share/tracks \  
&& sed -ri "0,/source/ a\\\\\ngem 'puma'" Gemfile \  
&& sed -ri "0,/source/ a\\\\\ngem 'tzinfo-data'" Gemfile \  
&& sed -ri "/gem \"mysql2\"/ s/^/#/" Gemfile \  
&& bundle install  
  
# Install configuration files  
COPY assets/config/ /usr/local/share/tracks/config/  
COPY assets/supervisor/ /etc/supervisor/conf.d/  
COPY assets/nginx/tracks /etc/nginx/sites-enabled/  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 80/tcp  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

