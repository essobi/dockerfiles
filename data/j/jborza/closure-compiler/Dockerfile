FROM alpine:3.5  
LABEL maintainer jborza  
COPY resources/cc.sh /opt/cc.sh  
RUN apk add \--no-cache --update openjdk8-jre curl unzip \  
&& curl https://dl.google.com/closure-compiler/compiler-latest.zip >>
/tmp/cc.zip \  
&& unzip -d /tmp /tmp/cc.zip c*.jar \  
&& cp /tmp/c*.jar /opt/closure-compiler.jar \  
&& rm /tmp/c*.jar \  
&& chmod +x /opt/cc.sh  
ENTRYPOINT ["/opt/cc.sh"]

