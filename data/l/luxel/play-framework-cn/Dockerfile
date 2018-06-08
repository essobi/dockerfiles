FROM frolvlad/alpine-oraclejdk8:slim  
  
ENV TIMEZONE Asia/Shanghai  
ENV PROJECT_HOME /app  
ENV ACTIVATOR_VERSION 1.3.10  
RUN apk add --no-cache bash curl  
# modify timezone  
RUN apk update && apk add tzdata \  
&& ls /usr/share/zoneinfo \  
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo ${TIMEZONE} > /etc/timezone \  
&& date  
  
# Download activator  
WORKDIR /  
RUN curl -O http://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VERSION}/typesafe-activator-${ACTIVATOR_VERSION}.zip &&
\  
unzip typesafe-activator-${ACTIVATOR_VERSION}.zip -d / && \  
rm typesafe-activator-${ACTIVATOR_VERSION}.zip && \  
chmod a+x /activator-dist-${ACTIVATOR_VERSION}/bin/activator  
ENV PATH $PATH:/activator-dist-${ACTIVATOR_VERSION}/bin  
  
EXPOSE 9000 8888  
RUN mkdir ${PROJECT_HOME}  
WORKDIR ${PROJECT_HOME}  
  
CMD ["activator", "run"]

