FROM debian:jessie  
MAINTAINER drupal-docker <info@drupaldocker.org>  
  
VOLUME /var/www/html  
WORKDIR /var/www/html  
  
ADD ./ /root/  
  
RUN apt-get update && apt-get install -y git \  
&& cd /root \  
&& find . -name "run.sh" -exec chmod +x {} \; \  
&& mkdir -p /root/.ssh \  
&& ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts \  
&& ssh-keyscan github.com >> /root/.ssh/known_hosts \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CLONE_URL="" \  
BRANCH="master" \  
SHA="HEAD" \  
DEPTH="20"  
CMD ["/root/run.sh"]  

