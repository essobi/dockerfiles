FROM mono  
  
MAINTAINER Seif Attar <iam@seifattar.net>  
  
ADD init.sh /usr/local/bin/init.sh  
ADD start-nginx.sh /usr/local/bin/start-nginx.sh  
  
RUN chmod a+x /usr/local/bin/init.sh \  
&& chmod a+x /usr/local/bin/start-nginx.sh \  
&& apt-get update \  
&& apt-get install ca-certificates wget nginx -y --no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/* \  
&& mkdir -p /etc/mono/registry /etc/mono/registry/LocalMachine \  
&& wget --ca-directory=/etc/ssl/certs -O /usr/local/bin/dumb-init
https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-
init_1.0.0_amd64 \  
&& chmod +x /usr/local/bin/dumb-init  
  
ADD config/default /etc/nginx/sites-available/  
EXPOSE 80  
ENTRYPOINT ["/usr/local/bin/init.sh"]  
CMD ["echo", "No CMD specified, set a CMD to run in your Dockerfile"]  

