FROM debian:wheezy  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
ca-certificates \  
bash \  
bash-completion \  
ncurses-base \  
vim \  
curl \  
procps && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD rootfs /  
  
ENV CRON_ENABLED false  
ENV TERM xterm  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["bash"]  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/dockhippie/debian.git"  
LABEL org.label-schema.name="Debian"  
LABEL org.label-schema.vendor="Thomas Boerger"  
LABEL org.label-schema.schema-version="1.0"  

