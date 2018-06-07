FROM datadog/docker-dd-agent:11.0.563  
# Install curl  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Rancher init script  
COPY entrypoint-rancher.sh /entrypoint.sh  

