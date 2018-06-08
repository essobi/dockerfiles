FROM nginx:1.12.2  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 /usr/local/bin/confd  
  
COPY confd /etc/confd  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT "entrypoint.sh"  
CMD [ "nginx" ]  
  
RUN rm /etc/nginx/conf.d/*  
  
# This file is used by the start script to substitute Templates  
#  
# Currently known Templates:  
# SERVER_URL: served url  
RUN mkdir -p /var/www/app  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV LC_ALL=C  
ENV LANG=C  
RUN apt-get update && apt-get -y install coreutils mysql-client locales \  
&& chmod +x /usr/local/bin/confd \  
&& rm -Rf /var/lib/apt/lists  
RUN localedef -i de_DE -f UTF-8 de_DE.UTF-8  
ENV LC_ALL=de_DE.UTF-8  
ENV LANG=de_DE.UTF-8  
ENV LANGUAGE=de_DE.UTF-8  
COPY include /etc/nginx/include  

