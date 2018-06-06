FROM openjdk:8-jre-slim  
  
ENV CEREBRO_VERSION=0.7.3  
RUN apt-get update \  
&& apt-get install -y wget \  
&& mkdir -p /usr/local/cerebro \  
&& wget -qO-
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz
\  
| tar xzv --strip-components 1 -C /usr/local/cerebro \  
&& groupadd --system cerebro \  
&& useradd --system --gid cerebro cerebro \  
&& chown -R cerebro:cerebro /usr/local/cerebro \  
&& apt-get remove -y --purge --auto-remove wget \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/local/cerebro  
USER cerebro  
CMD [ "/usr/local/cerebro/bin/cerebro" ]  

