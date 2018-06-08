FROM multiarch/alpine:x86-v3.7  
MAINTAINER Yves Schumann <yves@eisfair.org>  
  
# Define build arguments  
ARG DEVELOP_USER=developer  
ARG DEVELOP_PASS=developer  
  
# Define environment vars  
ENV WORK_DIR=/data/work  
  
# Mount point for development workspace  
RUN mkdir -p ${WORK_DIR}  
VOLUME ${WORK_DIR}  
RUN apk update \  
&& apk upgrade \  
&& apk add \  
alpine-sdk \  
bash \  
openssh \  
mc \  
sudo \  
rsync \  
autoconf \  
automake \  
libtool \  
flex \  
coreutils \  
ncurses-dev \  
linux-headers \  
openrc \  
tzdata \  
cmake \  
&& adduser -D -h /home/${DEVELOP_USER} -s /bin/bash -G abuild ${DEVELOP_USER}
\  
&& echo "${DEVELOP_USER}:${DEVELOP_PASS}" | chpasswd \  
&& echo "${DEVELOP_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& mkdir -p /var/cache/distfiles \  
&& chmod a+w /var/cache/distfiles \  
&& cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime \  
&& echo "Europe/Berlin" > /etc/timezone  
  
# Mount point for develop user home  
VOLUME /home/${DEVELOP_USER}  
# Mount point for global abuild configuration  
RUN mv /etc/abuild.conf /etc/abuild.conf.default  
  
#USER ${DEVELOP_USER}  

