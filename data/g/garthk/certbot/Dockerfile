FROM ubuntu:trusty  
ADD sources.list /etc/apt/  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl \  
&& apt-get clean ALL THE THINGS \  
&& curl -Lo /usr/local/bin/certbot-auto https://dl.eff.org/certbot-auto \  
&& chmod a+x /usr/local/bin/certbot-auto \  
&& /usr/local/bin/certbot-auto --non-interactive --version  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64 /usr/bin/dumb-init  
RUN chmod 0777 /usr/bin/dumb-init  
# Running dumb-init in non-setsid mode  
# https://github.com/Yelp/dumb-init/issues/51  
ENTRYPOINT ["/usr/bin/dumb-init", "-c", "--", "/usr/local/bin/certbot-auto"]  
VOLUME ["/etc/letsencrypt", "/var/log/letsencrypt", "/var/lib/letsencrypt"]  
CMD ["--help"]  

