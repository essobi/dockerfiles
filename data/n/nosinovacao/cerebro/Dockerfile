FROM openjdk:8-jre-alpine  
  
LABEL maintainer="NOS Inovação S.A."  
  
ENV CEREBRO_VERSION 0.7.2  
ENV CEREBRO_HOME /usr/share/cerebro  
  
# install dependencies  
RUN apk update && apk add bash  
  
# download  
RUN wget -O cerebro-${CEREBRO_VERSION}.tgz
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz
\  
&& tar zxvf cerebro-${CEREBRO_VERSION}.tgz \  
&& rm cerebro-${CEREBRO_VERSION}.tgz \  
&& mv cerebro-${CEREBRO_VERSION} ${CEREBRO_HOME}  
  
WORKDIR ${CEREBRO_HOME}  
  
EXPOSE 9000  
CMD ["bin/cerebro"]  

