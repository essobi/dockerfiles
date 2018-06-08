FROM spreadspace/ffmpeg:latest  
MAINTAINER Christian Pointner <equinox@spreadspace.org>  
  
USER root  
  
RUN set -x \  
&& echo 'deb http://deb.debian.org/debian stretch-backports main' >>
/etc/apt/sources.list \  
&& apt-get update -q \  
&& apt-get install -y -q -t stretch-backports nginx libnginx-mod-stream
libnginx-mod-rtmp libnginx-mod-http-lua \  
&& apt-get upgrade -y -q \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER app  

