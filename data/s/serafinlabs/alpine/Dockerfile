FROM alpine:3.7  
LABEL maintainer="Nicolas Degardin <degardin.n@gmail.com>"  
  
ENV PATH .:$PATH  
ENV TERM=xterm  
  
#RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
LC_CTYPE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8  
RUN apk add \--update --no-cache socat curl tzdata findutils  
RUN ln -fs /usr/share/zoneinfo/GMT /etc/localtime  
  
# Prepare dev tools  
ADD files/zshrc /opt/docker/zshrc  
ADD files/install-devtools.sh /opt/docker/install-devtools.sh  
ADD files/startup-timezone.sh /opt/docker/startup-timezone.sh  
  
RUN chmod 644 /opt/docker/zshrc  

