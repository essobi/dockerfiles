FROM gitlab/gitlab-runner:alpine  
MAINTAINER novaeye@qq.com  
  
ENV JAVA_HOME=/usr/lib/jvm/default-jvm  
  
RUN apk add \--no-cache openjdk8 && \  
adduser -D gitlab-runner && \  
ln -sf "${JAVA_HOME}/bin/"* "/usr/bin/"  

