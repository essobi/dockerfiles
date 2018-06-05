FROM alpine  
  
ENV RUNDECK_VERSION=2.10.0  
ENV RDECK_BASE=/etc/rundeck  
ENV RDECK_JAR=$RDECK_BASE/app.jar  
ENV PATH=$PATH:$RDECK_BASE/tools/bin  
  
RUN apk add --update openjdk8-jre bash curl ca-certificates openssh-client
ansible build-base libffi-dev ruby ruby-dev && \  
mkdir -p $RDECK_BASE && \  
rm -Rf /var/cache/apk/*  
  
RUN gem install winrm -v 2.2.3; exit 0  
RUN gem install winrm-fs -v 1.0.2; exit 0  
RUN gem install rubyntlm -v 0.6.2; exit 0  
  
# Download launcher & plugins  
## Production  
ADD http://dl.bintray.com/rundeck/rundeck-maven/rundeck-
launcher-${RUNDECK_VERSION}.jar /res/rundeck-launcher-${RUNDECK_VERSION}.jar  
ADD https://github.com/higanworks/rundeck-slack-incoming-webhook-
plugin/releases/download/v0.6.dev/rundeck-slack-incoming-webhook-
plugin-0.6.jar /res/plugin/rundeck-slack-incoming-webhook-plugin-0.6.jar  
ADD https://github.com/NetDocuments/rd-winrm-plugin/archive/1.7.0.zip
/res/plugin/rd-winrm-plugin-1.7.0.zip  
## Debug  
# COPY ./res/rundeck-launcher-${RUNDECK_VERSION}.jar /res/  
# COPY ./res/plugin /res/plugin  
COPY ./res/conf /res/conf  
COPY ./res/policy /res/policy  
  
COPY run.sh /bin/rundeck  
RUN chmod 0755 /bin/rundeck  
  
# Keystore  
RUN mkdir -p /var/lib/rundeck/.ssh  
RUN mkdir -p $RDECK_BASE/ssl  
  
# install dir  
# ssh-keys  
# logs  
VOLUME [ "$RDECK_BASE", "/var/lib/rundeck/.ssh", "$RDECK_BASE/server/logs" ]  
  
CMD rundeck

