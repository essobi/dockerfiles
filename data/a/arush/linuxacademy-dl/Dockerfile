FROM alpine  
ARG VCS_REF  
ARG BUILD_DATE  
LABEL maintainer "arush[dot]sal[at]gmail"  
LABEL org.label-schema.description="This image is used to start the
linuxacademy-dl executable." \  
org.label-schema.usage="docker run -it arush/linuxacademy-dl:latest -v <local-
directory>:/media" \  
org.label-schema.docker.cmd="docker run -it arush/linuxacademy-dl:latest -v
<local-directory>:/media" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="arush/linuxacademy-dl" \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.url="https://github.com/arush/linuxacademy-dl" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/arush/linuxacademy-dl" \  
org.label-schema.vendor="arush" \  
org.label-schema.version="1.0.1"  
ENV LC_ALL='en_US.UTF-8'  
ENV LANG='en_US.UTF-8'  
VOLUME ["/media"]  
RUN ["apk", "add", "--no-cache", "python2", "ffmpeg", "py-pip", "ca-
certificates"]  
COPY [".","/opt/linuxacademy-dl"]  
WORKDIR /opt/linuxacademy-dl  
RUN ["python2", "setup.py", "install"]  
WORKDIR /media  
ENTRYPOINT ["/bin/sh", "-i"]  

