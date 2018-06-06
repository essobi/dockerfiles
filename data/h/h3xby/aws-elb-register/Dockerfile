FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends awscli cloud-utils \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD start.sh /  
  
ENTRYPOINT ["/start.sh"]  
CMD ["register"]  

