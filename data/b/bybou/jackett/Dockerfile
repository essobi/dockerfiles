FROM xataz/mono  
MAINTAINER bybou <https://github.com/bybou>  
  
ENV UID=1000 GID=1000  
RUN apk add -U curl-dev \  
&& mkdir -p /opt \  
&& jack_tag=$(curl -sX GET
"https://api.github.com/repos/Jackett/Jackett/releases/latest" | awk
'/tag_name/{print $4;exit}' FS='[""]') \  
&& mkdir -p /opt \  
&& cd /opt \  
&& wget
https://github.com/Jackett/Jackett/releases/download/$jack_tag/Jackett.Binaries.Mono.tar.gz
\  
&& tar xzf Jackett.Binaries.Mono.tar.gz \  
&& rm -rf /opt/*.tar.gz /var/cache/apk/*  
  
EXPOSE 5000  
ADD startup /usr/bin/startup  
RUN chmod +x /usr/bin/startup  
  
CMD ["tini","--","startup"]  

