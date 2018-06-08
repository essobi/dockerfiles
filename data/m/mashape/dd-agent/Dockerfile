FROM datadog/docker-dd-agent  
  
RUN apt-get update && \  
apt-get install -y curl && \  
rm -rf /var/lib/apt/lists/* && \  
awk 'NR==4{print "sed -i -r -e \"s/HOST/$(curl -s
http://169.254.169.254/latest/meta-data/local-ipv4/)/\" /etc/dd-
agent/conf.d/auto_conf/*.yaml"}4' /entrypoint.sh > /tmp/entrypoint.sh && \  
mv /tmp/entrypoint.sh /entrypoint.sh && \  
chmod +x /entrypoint.sh  
  
# Add MySQL check configuration  
ADD http_check.yaml /etc/dd-agent/conf.d/auto_conf/http_check.yaml  
ADD nginx.yaml /etc/dd-agent/conf.d/auto_conf/nginx.yaml  

