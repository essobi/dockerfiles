FROM alpine  
  
ENV CLI_VERSION=0.4.1  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.12.6  
ENV DOCKER_SHA256
cadc6025c841e034506703a06cf54204e51d0cadfae4bae62628ac648d82efdd  
  
RUN apk add --update util-linux curl openssl ca-certificates bash && rm -rf
/var/cache/apk/*  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
  
ADD https://github.com/rancher/cli/releases/download/v${CLI_VERSION}/rancher-
linux-amd64-v${CLI_VERSION}.tar.gz /tmp/cli.tar.gz  
RUN tar xvfz /tmp/cli.tar.gz -C /tmp \  
&& cp "/tmp/rancher-v${CLI_VERSION}/rancher" /bin/ \  
&& rm -rf /tmp/*  
  
ENV PATH=/opt/rancher-deploy:$PATH  
COPY /scripts /opt/rancher-deploy/  
  
CMD ["bash"]

