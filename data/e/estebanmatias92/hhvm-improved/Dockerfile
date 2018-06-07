FROM estebanmatias92/hhvm:3.5-fastcgi  
  
MAINTAINER "Matias Esteban" <estebanmatias92@gmail.com>  
  
# Install "dockerize" http://github.com/jwilder/dockerize  
RUN wget -O /tmp/dockerize.tar.gz
https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-
amd64-v0.0.2.tar.gz \  
&& tar -C /usr/local/bin -xvzf /tmp/dockerize.tar.gz \  
&& rm /tmp/dockerize.tar.gz  
  
# Install hhvm extension dependencies  
RUN apt-get update && apt-get install -y libpq-dev && rm -r
/var/lib/apt/lists/* \  
&& libbson_version="1.0.0" \  
&& wget -O /tmp/libbson.tar.gz
https://github.com/mongodb/libbson/releases/download/$libbson_version/libbson-$libbson_version.tar.gz
\  
&& mkdir /tmp/libbson \  
&& tar -C /tmp/libbson -xvzf /tmp/libbson.tar.gz --strip-components=1 \  
&& rm /tmp/libbson.tar.gz \  
&& cd /tmp/libbson \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf $(pwd) \  
&& cd -  
  
# Install hhvm extensions  
RUN hhvm-ext-install mongofill/mongofill-hhvm dstelter/hhvm-pgsql  
  
CMD ["hhvm", "--mode", "server"]  

