FROM debian:jessie  
MAINTAINER Kuzzle <support@kuzzle.io>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
&& cd /tmp \  
&& curl -SLO https://releases.hashicorp.com/consul-template/0.19.3/consul-
template_0.19.3_linux_amd64.tgz \  
&& tar -xvf consul-template_0.19.3_linux_amd64.tgz \  
&& chmod a+x consul-template \  
&& mv consul-template /usr/local/bin/ \  
&& rm -rf consul-template* \  
\  
&& curl -SLO
https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz \  
&& tar -xvf docker-17.09.0-ce.tgz \  
&& mv docker/docker /usr/local/bin/ \  
&& rm -rf docker* \  
\  
&& apt-get purge -y --auto-remove \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT [ "consul-template" ]  
CMD [ "--help" ]  

