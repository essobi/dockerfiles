FROM docker:18.03.1-ce  
  
# Install basic tools: git, ssh, curl, ag, envsubst  
RUN apk add --no-cache git openssh curl the_silver_searcher gettext  
  
# Install docker-compose  
ENV DOCKER_COMPOSE_VERSION 1.21.1  
RUN apk add --no-cache openssl ca-certificates \  
&& curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk \  
&& apk add --no-cache glibc-2.23-r3.apk && rm glibc-2.23-r3.apk \  
&& ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \  
&& ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib  
  
# Install Kubernetes  
ENV KUBERNETES_VERSION 1.9.3  
RUN wget -q https://storage.googleapis.com/kubernetes-
release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl \  
&& chmod +x kubectl \  
&& mv kubectl /usr/bin  
  
# Install Kops  
ENV KOPS_VERSION 1.9.0  
RUN wget -q
https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-
linux-amd64 \  
&& chmod +x kops-linux-amd64 \  
&& mv kops-linux-amd64 /usr/bin/kops  
  
# Install AWS CLI  
RUN apk add --no-cache groff less python py-pip \  
&& pip install awscli \  
&& apk --purge del py-pip  
  
# Install Ruby  
RUN apk add --no-cache ruby  
  
# Add AWS config  
RUN mkdir -p /root/.aws  
ADD aws /root/.aws  
  
# Add scripts  
ADD scripts /usr/local/bin  
  
# Unset the entrypoint provided by the "docker" image. By default  
# it uses a start-up script that launches the docker daemon, which  
# we don't want.  
ENTRYPOINT []  

