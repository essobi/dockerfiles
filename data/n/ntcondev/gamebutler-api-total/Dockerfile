FROM nimmis/alpine-java:latest  
MAINTAINER NTCon<nt@ntcon.co>  
  
#ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8  
#ARG VERSION  
#ENV VERSION = $VERSION  
  
COPY /VERSION /VERSION  
COPY /java.sh /java.sh  
#ENV VERSION 1.0.2  
#RUN export VERSION=1.0.2  
#RUN export VERSION=$(cat /VERSION | xargs)  
#ENV VERSION $(cat /VERSION | xargs)  
#COPY /build/libs/ /  
#COPY  
WORKDIR /  
  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
#CMD ["./java.sh"]  
#RUN ["chmod", "+x", "./java.sh”]  
CMD './java.sh';  
#CMD ["java", "-jar", "gamebutler-api-total-$VERSION.jar"]  
#CMD java -jar gamebutler-api-total-$VERSION.jar  
  
EXPOSE 80

