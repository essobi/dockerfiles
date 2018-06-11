FROM alpine:latest  
LABEL authors="Vassim Shahir <https://github.com/vassim>, Sushant Salil
<https://github.com/arush-sal>"  
LABEL org.label-schema.description="This image is used to start the
linuxacademy-dl executable." \  
org.label-schema.usage="docker run -it vassim/linuxacademy-dl:latest -v
<local-directory>:/media" \  
org.label-schema.docker.cmd="docker run -it vassim/linuxacademy-dl:latest -v
<local-directory>:/media" \  
org.label-schema.name="vassim/linuxacademy-dl" \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.url="https://github.com/vassim/linuxacademy-dl" \  
org.label-schema.vcs-url="https://github.com/vassim/linuxacademy-dl" \  
org.label-schema.version="1.0.0"  
ENV LC_ALL='en_US.UTF-8'  
ENV LANG='en_US.UTF-8'  
VOLUME ["/media"]  
RUN ["apk", "add", "--update", "--no-cache", "python2", "ffmpeg", "py-pip",
"ca-certificates", "py-crypto"]  
COPY [".", "/opt/linuxacademy-dl"]  
WORKDIR /opt/linuxacademy-dl  
RUN ["python2", "setup.py", "install"]  
WORKDIR /media  
ENTRYPOINT ["/bin/sh", "-i"]

