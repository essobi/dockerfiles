FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
sudo \  
ntp \  
net-tools \  
telnet \  
git \  
gnupg2 \  
curl \  
apt-utils \  
daemon  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-add-repository -y ppa:nginx/stable \  
&& apt-get update \  
&& apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm /etc/nginx/sites-enabled/default  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | sudo bash
-  
RUN apt-get install --yes nodejs  
RUN apt-get install --yes build-essential  
RUN npm install -g bower -y  
RUN npm install -g grunt  
RUN npm install -g grunt-cli  
  
RUN groupadd -r dateperfect && useradd -r -g dateperfect dateperfect  
RUN groupadd -r nginx && useradd -r -g nginx nginx  
RUN chmod -R 775 /etc/nginx/sites-available && chown -R dateperfect:nginx
/etc/nginx/sites-available  
RUN chmod -R 775 /etc/nginx/sites-enabled && chown -R dateperfect:nginx
/etc/nginx/sites-enabled  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

