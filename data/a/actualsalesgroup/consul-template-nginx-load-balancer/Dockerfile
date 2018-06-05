FROM actualsalesgroup/consul-template:latest  
MAINTAINER devops@actualsalesgroup.com  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update -qq && \  
apt-get -y install libssl1.0.0 && \  
rm -rf /var/lib/apt/lists/*  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y clean && \  
apt-get -y autoclean  
  
ADD debs/openresty_1.11.2.2_amd64.deb /tmp/  
RUN dpkg -i /tmp/openresty_1.11.2.2_amd64.deb  
RUN rm -f /tmp/openresty_1.11.2.2_amd64.deb  
  
ADD services/openresty.service /etc/service/openresty/run  
RUN chmod a+x /etc/service/openresty/run  
ADD services/consul-template.service /etc/service/consul-template/run  
RUN chmod a+x /etc/service/consul-template/run  
  
RUN mkdir /var/cache/pgspeed  
RUN chown www-data:www-data /var/cache/pgspeed  
  
ADD consul-templates/app.conf /etc/consul-templates/app.conf  
ADD consul-templates/nginx.conf /etc/consul-templates/nginx.conf  
ADD lua/uuid4.lua /opt/openresty/nginx/lua/uuid4.lua  
RUN mkdir /opt/openresty/nginx/conf/conf.d  
ADD confs/status.conf /opt/openresty/nginx/conf/conf.d/status.conf  
RUN adduser --group --system --shell /bin/false \--no-create-home --disabled-
password --home /nonexistent nginx  
  
CMD ["/usr/bin/runsvdir", "/etc/service"]  

