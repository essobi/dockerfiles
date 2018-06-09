FROM debian:jessie  
MAINTAINER Steve Nolen <technolengy@gmail.com>  
  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y python3 python3-pip git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip3 install --upgrade git+https://github.com/yadayada/acd_cli.git  
  
RUN mkdir /root/.cache \  
&& mkdir /acd_data \  
&& mkdir /acd_cache \  
&& ln -s /acd_cache /root/.cache/acd_cli  
  
VOLUME ['/acd_cache', '/acd_data']  
CMD acd_cli sync && acd_cli upload $ARGS $SRC $DEST

