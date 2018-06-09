FROM alpine:3.6  
  
MAINTAINER Frank Mai <frank@rancher.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL \  
io.github.thxcode.build-date=$BUILD_DATE \  
io.github.thxcode.name="rabbitmq-plugins-box" \  
io.github.thxcode.description="Storing RabbitMQ plugins by Alpine." \  
io.github.thxcode.url="https://github.com/thxcode/rabbitmq-plugins-box" \  
io.github.thxcode.vcs-type="Git" \  
io.github.thxcode.vcs-ref=$VCS_REF \  
io.github.thxcode.vcs-url="https://github.com/thxcode/rabbitmq-plugins-
box.git" \  
io.github.thxcode.vendor="Rancher Labs, Inc" \  
io.github.thxcode.version=$VERSION \  
io.github.thxcode.schema-version="1.0" \  
io.github.thxcode.license="MIT" \  
io.github.thxcode.docker.dockerfile="/Dockerfile"  
  
ENV IS_BOX true  
  
RUN apk add --update --no-cache \  
dumb-init bash sudo \  
&& rm -fr /var/cache/apk/* \  
&& mkdir /plugins  
  
ADD [ "https://github.com/rabbitmq/rabbitmq-
autocluster/releases/download/0.10.0/autocluster-0.10.0.ez",
"https://github.com/rabbitmq/rabbitmq-
autocluster/releases/download/0.10.0/rabbitmq_aws-0.10.0.ez", "/plugins/"]  
  
CMD ["/bin/bash"]

