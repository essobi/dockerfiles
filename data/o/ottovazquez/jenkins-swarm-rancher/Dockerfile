FROM ottovazquez/jenkins-swarm:latest  
  
ENV RANCHER_CLI_VERSION="v0.6.7"  
ENV RANCHER_COMPOSE_VERSION="v0.12.5"  
  
ARG baseUrl="https://github.com/rancher"  
RUN
RANCHER_CLI_URL="${baseUrl}/cli/releases/download/${RANCHER_CLI_VERSION}/rancher-
linux-amd64-${RANCHER_CLI_VERSION}.tar.gz " &&\  
curl -fsSL ${RANCHER_CLI_URL} | tar \--strip-components=2 -xz -C
/usr/local/bin &&\  
RANCHER_COMPOSE_URL="${baseUrl}/rancher-
compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz" &&\  
curl -fsSL ${RANCHER_COMPOSE_URL} | tar \--strip-components=2 -xz -C
/usr/local/bin  

