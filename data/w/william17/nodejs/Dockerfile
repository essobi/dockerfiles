FROM william17/debian:latest  
MAINTAINER William Leung<superbill2012@qq.com>  
  
ENV PATH $PATH:/opt/nodejs/bin  
ENV VERSION v0.11.13  
RUN \  
mkdir -p /opt/nodejs && \  
wget -O -
"http://www.nodejs.org/dist/${VERSION}/node-${VERSION}-linux-x64.tar.gz" | tar
--strip-components=1 -C /opt/nodejs -x -z

