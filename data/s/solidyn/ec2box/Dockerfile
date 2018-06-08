FROM openjdk:8-jre-alpine  
  
ENV version="0.35.00"  
LABEL maintainer="Ian Martin <imartin@solidyn.com>" license="MIT"
vendor="Solidyn Solutions, Inc" \  
repo="https://github.com/solidyn/docker" version="${version}"  
  
RUN apk --no-cache add curl tar gzip && \  
adduser -D -u 9000 ec2box && \  
file=$(echo $version | sed 's/\\.\\([0-9]\\+\\)$/_\1/') && \  
curl -LO -#
https://github.com/skavanagh/EC2Box/releases/download/v${version}/ec2box-
jetty-v${file}.tar.gz && \  
tar xvf ec2box-jetty-v${file}.tar.gz -C / && \  
chown -R ec2box: /EC2Box-jetty && \  
rm -rf ec2box*  
  
USER ec2box  
EXPOSE 8443  
WORKDIR /EC2Box-jetty/jetty  
ENTRYPOINT ["java", "-Xmx1g", "-jar", "start.jar"]  

