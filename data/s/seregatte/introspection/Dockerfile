FROM python:alpine  
  
RUN apk add --no-cache \  
ca-certificates \  
curl \  
openssl \  
bash \  
git \  
openssh \  
rsync  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 17.03.0-ce  
ENV DOCKER_SHA256
4a9766d99c6818b2d54dc302db3c9f7b352ad0a80a2dc179ec164a3ba29c2d3e  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
  
RUN mkdir -p ~root/.ssh && chmod 700 ~root/.ssh/ && \  
echo -e "Port 22\n" >> /etc/ssh/sshd_config && \  
echo -e "PermitRootLogin yes" >> /etc/ssh/sshd_config && \  
cp -a /etc/ssh /etc/ssh.cache && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 22  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]  

