FROM pangpanglabs/java8  
  
MAINTAINER pangpanglab <pangpanglab@p2shop.cn>  
  
ENV PRESTO_VERSION 0.167  
RUN mkdir -p /opt/pangpang \  
&& mkdir -p /opt/pangpang/bin \  
&& curl -SL https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/${PRESTO_VERSION}/presto-server-${PRESTO_VERSION}.tar.gz \  
| tar -xzC /opt/pangpang  
  
RUN curl https://repo1.maven.org/maven2/com/facebook/presto/presto-
cli/${PRESTO_VERSION}/presto-cli-${PRESTO_VERSION}-executable.jar -o
/opt/pangpang/presto-server-${PRESTO_VERSION}/bin/presto  
RUN chmod a+x /opt/pangpang/presto-server-${PRESTO_VERSION}/bin/presto  
  
RUN apt-get update && apt-get install -y \  
python \  
uuid  

