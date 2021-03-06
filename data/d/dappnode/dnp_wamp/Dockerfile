FROM python:3-alpine  
  
# Metadata  
ARG CROSSBAR_VERSION  
ARG BUILD_DATE  
ARG CROSSBAR_VCS_REF  
  
# Metadata labeling  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Crossbar.io Starter Template" \  
org.label-schema.description="Quickstart template for application development
with Crossbar.io" \  
org.label-schema.url="http://crossbar.io" \  
org.label-schema.vcs-ref=$CROSSBAR_VCS_REF \  
org.label-schema.vcs-url="https://github.com/crossbario/crossbar" \  
org.label-schema.vendor="The Crossbar.io Project" \  
org.label-schema.version=$CROSSBAR_VERSION \  
org.label-schema.schema-version="1.0"  
# Application home  
ENV HOME /node  
ENV DEBIAN_FRONTEND noninteractive  
ENV PYTHONUNBUFFERED 1  
  
# install dependencies and Crossbar.io  
RUN apk --update upgrade \  
&& apk add libffi \  
&& apk add \--virtual .build-deps \  
build-base \  
libffi-dev \  
libressl-dev \  
linux-headers \  
&& pip install --no-cache-dir -U pip \  
&& pip install --no-cache-dir crossbar \  
&& apk del .build-deps  
  
# test if everything installed properly  
RUN crossbar version  
  
# add our user and group  
RUN addgroup -S -g 242 crossbar \  
&& adduser -S -u 242 -D -h /node -G crossbar -g "Crossbar.io Service" crossbar  
  
# initialize a Crossbar.io node  
COPY ./node/ /node/  
RUN chown -R crossbar:crossbar /node  
  
# make /node a volume to allow external configuration  
VOLUME /node  
  
# set the Crossbar.io node directory as working directory  
WORKDIR /node  
  
# run under this user, and expose default port  
USER crossbar  
EXPOSE 8080 8000  
  
# entrypoint for the Docker image is the Crossbar.io executable  
ENTRYPOINT ["crossbar", "start", "--cbdir", "/node/.crossbar"]

