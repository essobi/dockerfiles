FROM wisbyme/scratch-vm:latest  
  
LABEL maintainer="kenlea <kenlea@163.com>"  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Scratch-kids Runtime" \  
org.label-schema.description="Scratch-kids 运行环境" \  
org.label-schema.url="https://github.com/gorouter/src_dockerfile" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/gorouter/src_dockerfile" \  
org.label-schema.vendor="kenlea" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
RUN apt-get update -y \  
&& cd ~/Scratch/scratch-blocks \  
&& npm install \  
&& npm link \  
&& /sbin/install_clean  
  
  

