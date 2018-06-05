# https://hub.docker.com/_/alpine/  
FROM alpine  
  
MAINTAINER Instrumentisto Team <developer@instrumentisto.com>  
  
  
# Install Bash, make, cURL, Git.  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
tini ca-certificates \  
bash git make curl \  
rsync \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
  
# Install Docker CLI.  
RUN curl -fL -o /tmp/docker.tar.gz \  
https://download.docker.com/linux/static/edge/x86_64/docker-18.05.0-ce.tgz \  
&& tar -xvf /tmp/docker.tar.gz -C /tmp/ \  
\  
&& chmod +x /tmp/docker/docker \  
&& mv /tmp/docker/docker /usr/local/bin/ \  
\  
&& mkdir -p /usr/local/share/doc/docker/ \  
&& curl -fL -o /usr/local/share/doc/docker/LICENSE \  
https://raw.githubusercontent.com/docker/docker-
ce/v18.05.0-ce/components/cli/LICENSE \  
\  
&& rm -rf /tmp/*  
  
  
# Install Docker Compose CLI.  
RUN curl -fL -o /usr/local/bin/docker-compose \  
https://github.com/docker/compose/releases/download/1.21.2/docker-compose-
Linux-x86_64 \  
&& chmod +x /usr/local/bin/docker-compose \  
\  
&& mkdir -p /usr/local/share/doc/docker-compose/ \  
&& curl -fL -o /usr/local/share/doc/docker-compose/LICENSE \  
https://raw.githubusercontent.com/docker/compose/1.21.2/LICENSE \  
\  
# Download glibc compatible musl library for Docker Compose, see:  
# https://github.com/docker/compose/pull/3856  
&& curl -fL -o /etc/apk/keys/sgerrand.rsa.pub \  
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& latestReleaseTag=$(\  
curl -s https://api.github.com/repos/sgerrand/alpine-pkg-glibc/releases/latest
\  
| grep '"tag_name"' \  
| cut -d '"' -f4 \  
| tr -d '\n' ) \  
&& curl -fL -o /tmp/glibc-$latestReleaseTag.apk \  
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$latestReleaseTag/glibc-$latestReleaseTag.apk \  
&& apk add --no-cache /tmp/glibc-$latestReleaseTag.apk \  
&& ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \  
&& ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib/ \  
\  
# Install libgcc_s.so.1 for pthread_cancel to work, see:  
# https://github.com/instrumentisto/gitlab-builder-docker-image/issues/6  
&& apk add --update --no-cache libgcc \  
&& ln -s /usr/lib/libgcc_s.so.1 /usr/glibc-compat/lib/ \  
\  
&& rm -rf /var/cache/apk/* \  
/tmp/*  
  
  
# Install Kubernetes CLI.  
RUN curl -fL -o /usr/local/bin/kubectl \  
https://dl.k8s.io/release/v1.10.3/bin/linux/amd64/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
  
  
# Install Kubernetes Helm.  
RUN curl -fL -o /tmp/helm.tar.gz \  
https://kubernetes-helm.storage.googleapis.com/helm-v2.9.1-linux-amd64.tar.gz
\  
&& tar -xzf /tmp/helm.tar.gz -C /tmp/ \  
\  
&& chmod +x /tmp/linux-amd64/helm \  
&& mv /tmp/linux-amd64/helm /usr/local/bin/ \  
\  
&& mkdir -p /usr/local/share/doc/helm/ \  
&& mv /tmp/linux-amd64/LICENSE /usr/local/share/doc/helm/ \  
\  
&& rm -rf /tmp/*  
  
  
ENTRYPOINT ["/sbin/tini", "--"]  

