FROM frolvlad/alpine-oraclejdk8  
MAINTAINER Atsushi Nagase<a@ngs.io>  
  
ENV API_VERSION '39.0.5'  
RUN apk add --no-cache curl maven  
  
RUN mkdir /src  
WORKDIR /src  
RUN curl -Lo wsc-${API_VERSION}.tar.gz
https://github.com/forcedotcom/wsc/archive/${API_VERSION}.tar.gz && tar xvfz
wsc-${API_VERSION}.tar.gz  
  
WORKDIR /src/wsc-${API_VERSION}  
RUN mvn clean package -Dgpg.skip && mv target/*.jar $JAVA_HOME/lib  
RUN rm -rf /src && mkdir -p ${JAVA_HOME}/lib/force-com-wsdl /src/classes
/src/triggers /wsdl  
ADD entrypoint /entrypoint  
  
ENTRYPOINT ["/entrypoint/run.sh"]  

