FROM ubuntu  
  
LABEL maintainer "dmitry@pereslegin.ru"  
  
WORKDIR /app  
  
RUN apt-get update && apt-get dist-upgrade -y && apt-get install --no-install-
recommends --no-install-suggests -y \  
apt-utils \  
bash \  
build-essential \  
ca-certificates \  
curl \  
nginx  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
# RUN npm install npm@latest -g  
# RUN curl -O
http://ftp.de.debian.org/debian/pool/main/libp/libpng/libpng12-0_1.2.50-2+deb8u3_amd64.deb  
# RUN dpkg -i libpng12-0_1.2.50-2+deb8u3_amd64.deb  
ADD package.json /app/package.json  
RUN cd /app && npm install  
  
ADD . /app  
  
RUN ./node_modules/.bin/webpack -p  
  
RUN rm /etc/nginx/sites-enabled/default  
ADD ./nginx.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

