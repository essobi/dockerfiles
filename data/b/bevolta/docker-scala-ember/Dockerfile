FROM frolvlad/alpine-oraclejdk8:slim  
  
ENV SBT_VERSION=1.1.0 \  
EMBER_CLI_VERSION=2.16.2 \  
BOWER_VERSION=1.8.0 \  
LANG=C.UTF-8  
# Install libs needed by CircleCI  
RUN apk add --no-cache --update bash git openssh tar zip xz nodejs nodejs-npm
bc  
  
# Install ember and bower  
RUN npm i -g bower@$BOWER_VERSION ember-cli@$EMBER_CLI_VERSION  
  
# Install sbt  
RUN apk add --no-cache --virtual=build-dependencies curl && \  
curl -sL
"https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz"
| gunzip | tar -x -C /usr/local && \  
ln -s /usr/local/sbt/bin/sbt /usr/local/bin/sbt && \  
chmod 0755 /usr/local/bin/sbt && \  
apk del build-dependencies && \  
sbt sbtVersion  
  
# Install AWSEBCLI  
RUN apk --no-cache add py-pip groff less && \  
pip install --upgrade pip awsebcli && \  
rm -rf /tmp/* /root/.cache

