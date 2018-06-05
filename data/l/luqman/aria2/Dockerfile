FROM phusion/baseimage:0.9.19  
CMD ["/sbin/my_init"]  
  
MAINTAINER luqman  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN set -x \  
&& usermod -u 99 nobody \  
&& usermod -g 100 nobody \  
&& usermod -d /home nobody \  
&& chown -R nobody:users /home \  
&& apt-get update \  
&& apt-get install -y aria2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/downloads", "/config", "media"]  
EXPOSE 6800  
ENV ARIA2_dir /downloads  
ENV ARIA2_enable_rpc true  
ENV ARIA2_rpc_listen_all true  
ENV ARIA2_on_download_complete=/config/download-complete.sh  
ENV ARIA2_log=-  
  
ADD download-complete.sh /tmp/download-complete.sh  
  
RUN mkdir -p /etc/my_init.d  
ADD aria2.sh /etc/my_init.d/aria2.sh  

