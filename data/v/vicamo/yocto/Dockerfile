# GENERATED FROM DOCKERFILE.TEMPLATE. DO NOT EDIT.  
FROM buildpack-deps:sid  
  
MAINTAINER vicamo@gmail.com  
  
ENV YOCTO_USER=yocto  
ENV YOCTO_HOME=/home/${YOCTO_USER}  
  
RUN apt-get update -qq \  
&& apt-get install --no-install-recommends -y \  
ccache \  
chrpath \  
cpio \  
diffstat \  
gawk \  
iptables \  
locales \  
python3 \  
sudo \  
texinfo \  
&& apt-get clean \  
&& rm -f /var/lib/apt/lists/*_dists_*  
  
RUN sed -i -e 's,^# en_US,en_US,' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LANGUAGE  
  
RUN useradd --comment 'Yocto Development Account' \  
\--home ${YOCTO_HOME} \--create-home \  
\--shell /bin/bash \  
${YOCTO_USER} \  
&& (echo "${YOCTO_USER}:${YOCTO_USER}" | chpasswd) \  
&& adduser ${YOCTO_USER} sudo \  
&& (echo "${YOCTO_USER} ALL=NOPASSWD: ALL" > /etc/sudoers.d/${YOCTO_USER}) \  
&& chmod 0440 /etc/sudoers.d/${YOCTO_USER}  
  
VOLUME ["${YOCTO_HOME}"]  
WORKDIR ${YOCTO_HOME}  
ENV LANG=en_US.UTF-8  
USER ${YOCTO_USER}  

