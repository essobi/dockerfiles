FROM alpine:latest  
  
LABEL maintainer="Yves Blusseau <90z7oey02@sneakemail.com> (@blusseau)"  
  
ENV DEBUG=false \  
DOCKER_GEN_VERSION=0.7.6 \  
DOCKER_HOST=unix:///var/run/docker.sock  
  
# Install packages required by the image  
RUN apk add --update \  
bash \  
ca-certificates \  
curl \  
jq \  
openssl \  
&& rm /var/cache/apk/*  
  
# Install docker-gen  
ENV DOWNLOAD_URL https://github.com/rid/docker-gen-
multi/releases/download/${DOCKER_GEN_VERSION}/docker-gen-alpine-linux-
amd64-${DOCKER_GEN_VERSION}.tar.gz  
RUN wget -qO- $DOWNLOAD_URL | tar xvz -C /usr/local/bin  
  
# Install simp_le  
COPY /install_simp_le.sh /app/install_simp_le.sh  
RUN chmod +rx /app/install_simp_le.sh && sync && /app/install_simp_le.sh && rm
-f /app/install_simp_le.sh  
  
COPY /app/ /app/  
  
WORKDIR /app  
  
ENTRYPOINT [ "/bin/bash", "/app/entrypoint.sh" ]  
CMD [ "/bin/bash", "/app/start.sh" ]  

