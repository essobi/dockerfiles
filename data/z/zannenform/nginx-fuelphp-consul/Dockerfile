# Nginx  
# for  
# Multi host application  
# consul-template  
# fuelPHP  
#  
# consul と連携することでマルチホストアプリケーションサーバーに対応します。  
# docker run -itd -p 80:80 -p 443:443 --dns `docker inspect --format="{{
.NetworkSettings.IPAddress }}" [consulコンテナ]` nginx  
FROM ubuntu:14.04  
MAINTAINER zanenform  
  
# Install Nginx.  
RUN apt-get -y update && apt-get install -y nginx  
  
# Install consul-template.  
RUN apt-get install -y golang git make && \  
export GOPATH="/usr/share/go/" && \  
cd /usr/local/src && \  
git clone https://github.com/hashicorp/consul-template.git && \  
cd consul-template && \  
make && \  
cp ./bin/consul-template /usr/bin/  
  
# Copy consul-template file.  
COPY site.ctmpl /etc/nginx/site.ctmpl  
  
# Expose ports.  
EXPOSE 80 443  
# Define default command.  
CMD ["/usr/bin/consul-template", "-consul consul.service.consul:8500 -template
/etc/nginx/nginx.ctmpl:/etc/nginx/sites-available/nginx.conf:service nginx
restart"]  

