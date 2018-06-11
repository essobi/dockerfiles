FROM ubuntu:rolling  
  
LABEL maintainer="Evgeny Orekhov <orehov@web-canape.com>"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends exim4-daemon-light \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY update-exim4.conf.conf /etc/exim4/  
  
COPY 00_local_macros /etc/exim4/conf.d/main/  
  
RUN echo smtp_accept_queue_per_connection=100 >>
/etc/exim4/conf.d/main/02_exim4-config_options  
  
RUN update-exim4.conf  
  
CMD ["exim", "-bd", "-q15m", "-v"]  

