FROM frolvlad/alpine-oraclejdk8:slim  
  
ENV SBT_VERSION 1.0.2  
ENV SBT_HOME /usr/share/sbt  
  
# Define working directory  
RUN mkdir -p /project  
WORKDIR /project  
  
RUN apk add --no-cache wget curl ca-certificates tini bash  
  
# install sbt  
RUN mkdir -p "${SBT_HOME}" && \  
wget -O -
"https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz"
| tar xz -C ${SBT_HOME} \--strip-components=1 && \  
ln -s "${SBT_HOME}/bin/"* "/usr/bin/"  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/sbt"]  

