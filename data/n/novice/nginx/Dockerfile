FROM ubuntu:latest  
MAINTAINER David <david@cninone.com>  
  
# Get noninteractive frontend for Debian to avoid some problems:  
# debconf: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y openssh-server software-properties-
common python-software-properties supervisor curl nano  
  
RUN mkdir -p /var/run/sshd /var/log/supervisor /var/log/nginx  
  
RUN echo 'root:freego' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# nginx  
RUN printf '%s\n%s\n' "deb http://nginx.org/packages/mainline/ubuntu/ trusty
nginx" "deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >>
/etc/apt/sources.list  
RUN wget -qO - http://nginx.org/keys/nginx_signing.key | apt-key add -  
RUN apt-get update && apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY nginx/index.html /var/www/index.html  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY nginx/freego.crt /etc/ssl/freego.crt  
COPY nginx/freego.key /etc/ssl/freego.key  
  
RUN chown -R www-data:www-data /var/www  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 22 80 443  
CMD ["/usr/bin/supervisord"]  

