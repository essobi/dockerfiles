FROM edwxie/jdk  
MAINTAINER Edward Xie <waterscar@gmail.com>  
  
# Activator version  
ENV VERSION 1.3.10  
# Download and unarchive Java  
RUN mkdir -p /opt && mkdir -p /code && cd /opt &&\  
curl https://downloads.typesafe.com/typesafe-activator/${VERSION}/typesafe-
activator-${VERSION}-minimal.zip -O &&\  
unzip typesafe-activator-${VERSION}-minimal.zip && ln -s
/opt/activator-${VERSION}-minimal /opt/activator &&\  
rm -rf typesafe-activator-${VERSION}-minimal.zip  
  
ENV PATH ${PATH}:/opt/activator/bin  
  
VOLUME ["/root/.ivy2/","/root/.sbt/", "/code"]  
  
WORKDIR /code  
  
# ENTRYPOINT activator  

