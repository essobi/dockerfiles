FROM java:8-jdk-alpine  
ENV CHECKSTYLE_VERSION=7.6.1  
RUN apk add --update \  
curl \  
&& rm -rf /var/cache/apk/*  
  
# Download the latest checkstyle release  
RUN curl -sLO \  
https://sourceforge.net/projects/checkstyle/files/checkstyle/${CHECKSTYLE_VERSION}/checkstyle-${CHECKSTYLE_VERSION}-all.jar
&& \  
mv checkstyle-*.jar /usr/bin/checkstyle.jar  
  
# for whalebrew  
LABEL io.whalebrew.name 'checkstyle'  
  
WORKDIR /workdir  
  
ENTRYPOINT ["java","-jar","/usr/bin/checkstyle.jar"]  
CMD ["-h"]  

