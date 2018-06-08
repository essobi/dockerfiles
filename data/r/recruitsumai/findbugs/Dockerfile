FROM java:8-jdk-alpine  
ENV FINDBUGS_VERSION=3.0.1  
WORKDIR /usr/workdir  
RUN apk add --update \  
curl \  
&& rm -rf /var/cache/apk/*  
  
# Download the latest findbugs release  
RUN curl -sL \  
https://sourceforge.net/projects/findbugs/files/findbugs/${FINDBUGS_VERSION}/findbugs-${FINDBUGS_VERSION}.tar.gz/download
| \  
tar -xz && \  
mv findbugs-* /usr/bin/findbugs  
  
# for whalebrew  
LABEL io.whalebrew.name 'findbugs'  
  
WORKDIR /workdir  
  
ENTRYPOINT ["java","-jar","/usr/bin/findbugs/lib/findbugs.jar"]  
CMD ["-h"]  
  

