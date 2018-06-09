FROM teffcz/debian:latest  
MAINTAINER Tomas Effenberger <effik@effik.cz>  
ENV PATH $PATH:/opt/nodejs/bin  
ENV VERSION v0.12.0  
RUN mkdir /opt/nodejs && \  
wget -O -
"http://www.nodejs.org/dist/${VERSION}/node-${VERSION}-linux-x64.tar.gz" | tar
\--directory=/opt/nodejs \--strip-components=1 -x -z  

