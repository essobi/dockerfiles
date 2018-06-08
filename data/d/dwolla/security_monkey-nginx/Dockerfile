FROM nginx:1.13.0  
MAINTAINER dev@dwolla.com  
  
ENV SECURITY_MONKEY_VERSION=v0.9.1  
RUN apt-get update &&\  
apt-get install -y curl git sudo apt-transport-https gnupg &&\  
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&\  
curl
https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list
> /etc/apt/sources.list.d/dart_stable.list && \  
apt-get update &&\  
apt-get install -y -q dart &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /usr/local/src &&\  
git clone -b $SECURITY_MONKEY_VERSION
https://github.com/Netflix/security_monkey.git &&\  
mkdir -p security_monkey  
  
RUN cd /usr/local/src/security_monkey/dart &&\  
/usr/lib/dart/bin/pub get &&\  
/usr/lib/dart/bin/pub build &&\  
/bin/mkdir -p /usr/local/src/security_monkey/security_monkey/static/ &&\  
/bin/cp -R /usr/local/src/security_monkey/dart/build/web/*
/usr/local/src/security_monkey/security_monkey/static/  
  
RUN /bin/rm /etc/nginx/conf.d/default.conf &&\  
/bin/mkdir -p /var/log/security_monkey/ /etc/nginx/ssl/ &&\  
ln -s /dev/stdout /var/log/security_monkey/security_monkey.access.log &&\  
ln -s /dev/stderr /var/log/security_monkey/security_monkey.error.log  
  
WORKDIR /etc/nginx  
EXPOSE 443  
ADD securitymonkey.conf /etc/nginx/conf.d/securitymonkey.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
ADD start-nginx.sh /usr/local/src/security_monkey/docker/nginx/start-nginx.sh  
RUN chmod +x /usr/local/src/security_monkey/docker/nginx/start-nginx.sh  
  
ENTRYPOINT ["/usr/local/src/security_monkey/docker/nginx/start-nginx.sh"]  

