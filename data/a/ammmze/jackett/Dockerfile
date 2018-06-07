FROM mono:3.10  
MAINTAINER ammmze <ammmze@gmail.com>  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& apt-get update -q \  
&& apt-get install -qy libcurl4-openssl-dev unzip wget \  
&& apt-get clean \  
&& wget
https://github.com/zone117x/Jackett/releases/download/v0.3.1/Release.v0.3.1.zip
-O /tmp/jackett.zip \  
&& unzip /tmp/jackett.zip -d /tmp/jackett \  
&& mv /tmp/jackett/Release /app \  
&& chown -R nobody:users /app \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /config \  
&& chown -R nobody:users /config \  
&& ln -s /config /usr/share/Jackett  
  
EXPOSE 9117  
VOLUME /config  
VOLUME /app  
  
ADD start.sh /  
RUN chmod +x /start.sh  
  
# Currently there is a bug in Jackett where running as non-root user causes
the app to not start up  
# See: https://github.com/zone117x/Jackett/issues/37  
# We could potentially start it initially as root and then kill it and then
start as nobody, but for now, hoping  
# the bug gets resolved.  
#USER nobody  
WORKDIR /app  
  
ENTRYPOINT ["/start.sh"]  

