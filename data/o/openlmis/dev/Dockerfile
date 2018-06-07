FROM anapsix/alpine-java:8u151b12_jdk  
  
WORKDIR /root  
  
COPY install_gradle.sh .  
ENV GRADLE_USER_HOME /gradle  
ENV GRADLE_OPTS -Dorg.gradle.daemon=true  
  
RUN apk update && \  
apk add libstdc++ && \  
apk add bash && \  
apk add postgresql-client && \  
apk add postgresql && \  
apk add nodejs-current-npm && \  
apk add wget && \  
apk add py-pip && \  
pip install --upgrade pip && \  
pip install transifex-client && \  
mkdir bin && \  
npm install -g raml-cop@5.0.0 && \  
/bin/sh install_gradle.sh  
  
WORKDIR /app  
  
COPY sync_transifex.sh /transifex/sync_transifex.sh  
VOLUME ["/app", "/gradle"]  
  
EXPOSE 8080  
CMD ["bash"]  

