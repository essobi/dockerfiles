FROM alpine:3.4  
ENV VERSION v1.8.1  
ENV DUMB_INIT_VERSION 1.1.3  
ENV DOCKER_MACHINE_VERSION v0.8.1  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Custom gitlab-ci-multi-runner" \  
org.label-schema.description="GitLab Runner" \  
org.label-schema.url="https://gitlab.com/gitlab-org/gitlab-ci-multi-runner" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/skilld-labs/gitlab-runner" \  
org.label-schema.vendor="Skilld" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ADD entrypoint /  
  
RUN chmod +x /entrypoint && \  
apk add --update \  
bash \  
ca-certificates \  
git \  
openssl \  
wget && \  
wget https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 \  
-O /usr/bin/dumb-init && \  
chmod +x /usr/bin/dumb-init && \  
wget
https://github.com/docker/machine/releases/download/${DOCKER_MACHINE_VERSION}/docker-
machine-Linux-x86_64 \  
-O /usr/bin/docker-machine && \  
chmod +x /usr/bin/docker-machine && \  
wget https://gitlab-ci-multi-runner-
downloads.s3.amazonaws.com/${VERSION}/binaries/gitlab-ci-multi-runner-linux-
amd64 \  
-O /usr/bin/gitlab-ci-multi-runner && \  
chmod +x /usr/bin/gitlab-ci-multi-runner && \  
ln -s /usr/bin/gitlab-ci-multi-runner /usr/bin/gitlab-runner && \  
mkdir -p /etc/gitlab-runner/certs && \  
chmod -R 700 /etc/gitlab-runner && \  
rm -rf /var/cache/apk/*  
  
VOLUME ["/etc/gitlab-runner", "/home/gitlab-runner"]  
ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]  
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]  

