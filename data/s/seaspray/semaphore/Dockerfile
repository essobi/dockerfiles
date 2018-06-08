FROM alpine:3.5  
ENV SEMAPHORE_VERSION="2.4.1" SEMAPHORE_ARCH="linux_amd64"  
RUN apk add --no-cache git py2-pip mysql-client curl openssh-client tini
build-base libffi-dev python-dev openssl-dev && \  
pip install git+https://github.com/ansible/ansible.git@devel && \  
curl -sSfL "https://github.com/ansible-
semaphore/semaphore/releases/download/v$SEMAPHORE_VERSION/semaphore_$SEMAPHORE_ARCH"
> /usr/bin/semaphore && \  
chmod +x /usr/bin/semaphore && mkdir -p /etc/semaphore/playbooks  
  
EXPOSE 3000  
ADD ./scripts/docker-startup.sh /usr/bin/semaphore-startup.sh  
RUN chmod +x /usr/bin/semaphore-startup.sh  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["/usr/bin/semaphore-startup.sh", "/usr/bin/semaphore", "-config",
"/etc/semaphore/semaphore_config.json"]  

