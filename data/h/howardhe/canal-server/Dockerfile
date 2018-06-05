FROM java:8  
MAINTAINER Howard He "howard.he0329@gmail.com"  
ENV CANAL_VERSION=1.0.24  
ADD
https://github.com/alibaba/canal/releases/download/canal-${CANAL_VERSION}/canal.deployer-${CANAL_VERSION}.tar.gz
/tmp  
  
RUN cd /tmp && \  
mkdir canal && \  
tar zxvf canal.deployer-${CANAL_VERSION}.tar.gz -C /tmp/canal && \  
mv canal /  
  
WORKDIR /canal  
  
ENTRYPOINT ["bin/startup.sh"]

