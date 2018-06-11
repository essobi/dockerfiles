############################################################  
# Dockerfile for weka with wekaServer (as master)  
############################################################  
  
FROM gliderlabs/alpine:3.3  
MAINTAINER Kevin Rojczyk <kevin.roj@p8h.de>  
  
RUN apk --no-cache add openjdk8-jre wget zip  
  
WORKDIR /weka_server  
RUN wget -qO- -O tmp.zip
https://prdownloads.sourceforge.net/weka/weka-3-7-13.zip  
RUN unzip -q tmp.zip  
RUN rm tmp.zip  
WORKDIR /weka_server/weka-3-7-13  
RUN rm -r wekaexamples.zip weka-src.jar WekaManual.pdf  
ENV CLASSPATH /weka_server/weka-3-7-13/weka.jar  
RUN java weka.core.WekaPackageManager -install-package wekaServer  
RUN java weka.core.WekaPackageManager -install-package gridSearch  
RUN java weka.core.WekaPackageManager -install-package LibSVM  
  
EXPOSE 8085  
CMD ["java", "-Djava.awt.headless=true", "weka.Run", "WekaServer", "-slots",
"14"]  
  
  

