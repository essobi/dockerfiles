FROM java:openjdk-8-alpine  
MAINTAINER Shintaro Kaneko <kaneshin0120@gmail.com>  
  
ENV KOTLIN_VERSION 1.0.6  
ENV KOTLIN_HOME=/usr/local/share/kotlinc  
ENV KOTLIN_COMPILER_ARCHIVE kotlin-compiler-${KOTLIN_VERSION}.zip  
ENV KOTLIN_COMPILER_URL
https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/${KOTLIN_COMPILER_ARCHIVE}  
  
WORKDIR /tmp  
  
RUN apk add --update bash openssl && rm -rf /var/cache/apk/*  
  
RUN mkdir -p $(dirname ${KOTLIN_HOME}) \  
&& wget ${KOTLIN_COMPILER_URL} -O /tmp/${KOTLIN_COMPILER_ARCHIVE} \  
  
&& unzip /tmp/${KOTLIN_COMPILER_ARCHIVE} -d $(dirname ${KOTLIN_HOME}) \  
  
&& chmod 0755 \  
${KOTLIN_HOME}/bin/kotlin \  
${KOTLIN_HOME}/bin/kotlinc \  
${KOTLIN_HOME}/bin/kotlinc-js \  
${KOTLIN_HOME}/bin/kotlinc-jvm \  
  
&& rm -rf /tmp/${KOTLIN_COMPILER_ARCHIVE}  
  
ENV PATH $PATH:${KOTLIN_HOME}/bin  
  
RUN echo "fun main(args: Array<String>) { println(\"Hello, World!\") }" >
/tmp/hello.kt  
RUN kotlinc /tmp/hello.kt -include-runtime -d /tmp/hello.jar  

