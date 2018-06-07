FROM alpine:3.7  
# Run java  
RUN apk --update add openjdk8-jre  
  
# Port bindings  
ENV kangaroo.port=8080  
ENV kangaroo.host=0.0.0.0  
# Volume construction  
CMD mkdir -p /var/lib/kangaroo  
VOLUME /var/lib/kangaroo  
  
# Runtime environment  
EXPOSE 8080  
WORKDIR /root  
CMD ["/usr/bin/java", "-jar", "/root/kangaroo-server-authz.jar"]  
  
# Executable  
ARG KANGAROO_VERSION=1.2.1  
ADD https://repo.maven.apache.org/maven2/net/krotscheck/kangaroo-server-
authz/${KANGAROO_VERSION}/kangaroo-server-authz-${KANGAROO_VERSION}-jar-with-
dependencies.jar kangaroo-server-authz.jar  

