FROM shurshun/alpine-moscow  
  
LABEL author "Korviakov Andrey"  
LABEL maintainer "4lifenet@gmail.com"  
  
LABEL SERVICE_NAME="docker-event-bridge"  
  
RUN \  
DOCKER_EB_VERSION=$(curl -s https://api.github.com/repos/shurshun/docker-
event-bridge/tags | jq -r ".[0] .name") \  
&& curl -fSlL https://github.com/shurshun/docker-event-
bridge/releases/download/${DOCKER_EB_VERSION}/docker-event-
bridge_${DOCKER_EB_VERSION}_linux_amd64.tar.gz | tar -C /bin -zx  
  
ENTRYPOINT ["docker-event-bridge"]

