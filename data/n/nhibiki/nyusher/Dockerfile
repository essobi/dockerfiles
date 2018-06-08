FROM alpine:latest  
MAINTAINER NYUSHer https://github.com/NYUSHer  
  
RUN apk add --no-cache \  
ca-certificates \  
curl \  
bzip2-dev \  
gcc \  
sqlite \  
sqlite-dev \  
openssl \  
openssl-dev \  
git \  
screen \  
python3 \  
python3-dev \  
mysql \  
mysql-client \  
zsh  
  
RUN addgroup mysql mysql  
  
RUN pip3 install flask \  
flask-sqlalchemy \  
pymysql \  
flask-mail  
  
RUN git clone https://github.com/NYUSHer/backend /backend  
  
EXPOSE 3306  
EXPOSE 8080  
EXPOSE 8043  

