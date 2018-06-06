FROM alpine:latest  
  
ARG DATE=20180506  
ENV DATE=${DATE}  
ENV URL_TEMPLATE="http://dl.google.com/closure-
compiler/compiler-${DATE}.tar.gz"  
RUN apk add --no-cache openjdk8-jre wget make  
  
RUN mkdir -p /usr/local /tmp/closure/extract  
  
COPY scripts/closure-compiler.sh /usr/local/bin/closure-compiler  
RUN chmod +x /usr/local/bin/closure-compiler  
  
RUN wget -q -O /tmp/closure.tar.gz "${URL_TEMPLATE}" && \  
mkdir -p /tmp/closure/extract && \  
tar -xvf /tmp/closure.tar.gz -C /tmp/closure/extract && \  
cp -v /tmp/closure/extract/closure-compiler*.jar /usr/local/closure-
compiler.jar && \  
rm -rvf /tmp/closure.tar.gz /tmp/closure/extract  
  
ENTRYPOINT ["java", "-jar", "/usr/local/closure-compiler.jar"]  

