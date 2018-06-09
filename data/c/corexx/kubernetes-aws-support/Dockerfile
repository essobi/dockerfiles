FROM alpine:3.6  
MAINTAINER Viktor Oppitz <viktor.oppitz@corexx.io>  
  
# upgrade packages  
RUN apk --no-cache --quiet --available upgrade  
  
# create system-group "corexx" with group id 60000  
# create system-user "corexx" with user id 60000  
# - with no password (-D)  
# - with home directory (-H, -h /home)  
# - with group "corexx" (-G)  
RUN addgroup -S -g 60000 corexx && \  
adduser -S -D -H -h /home -G corexx -s /sbin/nologin -u 60000 -g "Corexx
Platform User" corexx  
  
# configure profile  
COPY assets/etc/profile /etc/profile  
ENV ENV /etc/profile  
  
# configure message of the day  
COPY assets/etc/profile.d/motd.sh /etc/profile.d/motd.sh  
  
# enable color prompt  
RUN rm /etc/profile.d/color_prompt  
COPY assets/etc/profile.d/color-prompt.sh /etc/profile.d/color-prompt.sh  
  
# create build timestamp  
RUN echo "TIMESTAMP=\"$(date +"%Y/%m/%d %H:%M:%S %Z")\"" >> /etc/os-release  
  
# create /opt, /data and /logs directory  
RUN mkdir /opt /data /logs && \  
chown corexx:corexx /home /data /logs  
  
# define default volumes  
VOLUME /home  
VOLUME /data  
VOLUME /logs  
VOLUME /tmp  
  
RUN apk add --no-cache ca-certificates  
  
# define package  
ENV PACKAGE bitbucket.org/corexx/kubernetes-aws-support  
  
# add go sources  
COPY *.go /go/src/${PACKAGE}/  
  
# compile and install app  
RUN apk add --no-cache --quiet --virtual .build-deps \  
go git libc-dev && \  
# setup go path  
export GOPATH=/go && \  
# compile app  
go get -d ${PACKAGE} && \  
go install ${PACKAGE} && \  
# install app  
mv /go/bin/$(echo ${PACKAGE} | awk -F\/ '{print $NF}') / && \  
# remove build dependencies  
rm -rf /go && \  
apk del .build-deps  
  
  
# apply application information  
RUN echo "NAME=\"Kubernetes AWS Support\"" > /etc/application-release && \  
echo "DESCRIPTION=\"AWS Support for Kubernetes Cluster\"" >> /etc/application-
release && \  
echo "TIMESTAMP=\"$(date +"%Y/%m/%d %H:%M:%S %Z")\"" >> /etc/application-
release  
  
# all commands/entrypoints shall run as user "corexx"  
USER corexx  
  
  
# define command  
CMD ["/kubernetes-aws-support"]

