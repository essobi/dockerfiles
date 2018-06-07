FROM debian:stable-slim  
  
LABEL Author="Lee Myring <mail@thinkstack.io>"  
LABEL Maintainer="Lee Myring"  
LABEL Description="kpcli wrapper instance"  
LABEL Version="0.2"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends kpcli \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir -p /keepassx  
  
WORKDIR /keepassx  
VOLUME /keepassx  
  
COPY ./bin/ /bin  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  

