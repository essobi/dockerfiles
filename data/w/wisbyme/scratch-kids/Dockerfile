FROM wisbyme/scratch-blocks:latest  
  
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
  
COPY 01_start_scratch.sh /etc/my_init.d/01_start_scratch.sh  
  
RUN apt-get update -y \  
&& chmod +x /etc/my_init.d/01_start_scratch.sh \  
&& cd ~/Scratch/scratch-gui \  
&& npm install \  
&& npm link scratch-vm scratch-blocks \  
&& npm install \  
&& /sbin/install_clean  
  
EXPOSE 80  
  
WORKDIR ~  

