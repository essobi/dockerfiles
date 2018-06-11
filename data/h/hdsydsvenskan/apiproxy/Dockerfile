FROM hdsydsvenskan/luanginx:1.10-alpine  
  
ENV CONSUL_TEMPLATE_VERSION 0.16.0  
# Add bash so that we can exec consul-template in the  
# shell script.  
RUN apk add --no-cache bash openssl && \  
wget https://releases.hashicorp.com/consul-template/0.16.0/consul-
template_0.16.0_linux_amd64.zip && \  
unzip consul-template_0.16.0_linux_amd64.zip && \  
mv consul-template /usr/local/bin/ && \  
rm consul-template_0.16.0_linux_amd64.zip  
  
ENV CONSUL "172.17.0.1:8500"  
COPY nginx.conf.ctmpl /etc/nginx/nginx.conf.ctmpl  
COPY run.sh /run.sh  
COPY prometheus.lua /nginx-prometheus/prometheus.lua  
  
CMD ["/run.sh"]

