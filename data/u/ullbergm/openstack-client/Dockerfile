FROM python:alpine as builder  
MAINTAINER Magnus Ullberg <magnus@ullberg.us>  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="openstack-client" \  
org.label-schema.description="Openstack client" \  
org.label-schema.url="http://ullberg.us/docker/openstack-client" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ullbergm/docker-openstack-client"
\  
org.label-schema.vendor="Magnus Ullberg" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
RUN apk add --update \--no-cache git build-base linux-headers libffi-dev
openssl-dev  
RUN git clone --depth 1 https://github.com/openstack/python-
openstackclient.git /src  
RUN cd /src && pip install --no-cache-dir \--root=/app .  
  
FROM python:alpine as latest  
COPY \--from=builder /app /  

