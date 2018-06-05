FROM alpine:3.7  
RUN apk add --no-cache gcc git make musl-dev  
RUN cd /tmp &&\  
git clone https://github.com/frohoff/grepcidr.git &&\  
cd /tmp/grepcidr &&\  
make grepcidr  
  
FROM alpine:3.7  
ARG BUILD_DATE  
ARG SOURCE_REF  
ARG SOURCE_TYPE  
  
RUN apk add --no-cache jq curl py-pip python openssh &&\  
pip install --upgrade awscli pip &&\  
rm -rf /tmp/* &&\  
mkdir /root/.aws && chmod 700 /root/.aws  
  
COPY \--from=0 /tmp/grepcidr/grepcidr /usr/bin/grepcidr  
  
WORKDIR /  
ADD entrypoint.sh *.json /  
ENV ADDRESS_CIDR=0.0.0.0/0 ADDRESS_CIDR6=::/0  
ENTRYPOINT ["/entrypoint.sh"]  
VOLUME ["/root/.aws"]  
  
LABEL maintainer="Patrick Double <pat@patdouble.com>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.vendor="https://github.com/double16" \  
org.label-schema.name="aws-ecs-route53-presence" \  
org.label-schema.url="https://github.com/double16/aws-ecs-route53-presence" \  
org.label-schema.docker.dockerfile="Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type=$SOURCE_TYPE \  
org.label-schema.vcs-url="https://github.com/double16/aws-ecs-
route53-presence.git"  

