FROM debian:jessie  
EXPOSE 80  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache &&
echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && echo
'Acquire::Languages "none;";' > /etc/apt/apt.conf.d/no-lang && apt-get update
&& apt-get install curl -y && echo 'deb http://httpredir.debian.org/debian
jessie-backports main' >> /etc/apt/sources.list && curl -sL
https://deb.nodesource.com/setup_5.x | bash - && apt-get install nginx -y &&
apt-get install nodejs -y && apt-get clean  
COPY nginx.conf /etc/nginx/nginx.conf  

