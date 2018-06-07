FROM debian:8.0  
MAINTAINER andystanton  
ENV LANG C.UTF-8  
ENV GNUSTEP_MAKE_VERSION 2.6.6  
ENV GNUSTEP_BASE_VERSION 1.24.7  
RUN apt-get update -qq  
RUN apt-get install -y \  
patch wget gobjc make libffi6 libffi-dev libxml2 \  
libxml2-dev libxslt1.1 libxslt1-dev libicu-dev && \  
wget \  
http://ftpmain.gnustep.org/pub/gnustep/core/gnustep-
make-${GNUSTEP_MAKE_VERSION}.tar.gz \  
http://ftpmain.gnustep.org/pub/gnustep/core/gnustep-
base-${GNUSTEP_BASE_VERSION}.tar.gz && \  
tar -xvf gnustep-make-${GNUSTEP_MAKE_VERSION}.tar.gz && \  
tar -xvf gnustep-base-${GNUSTEP_BASE_VERSION}.tar.gz && \  
cd /gnustep-make-${GNUSTEP_MAKE_VERSION} && ./configure && make && make
install && \  
cd /gnustep-base-${GNUSTEP_BASE_VERSION} && ./configure --disable-tls && make
&& make install && \  
printf "\n%s\n" "source /usr/local/share/GNUstep/Makefiles/GNUstep.sh" >>
/etc/bash.bashrc && \  
printf "\n%s\n" "source /usr/local/share/GNUstep/Makefiles/GNUstep.sh" >>
/etc/profile && \  
printf "\n%s\n" "export OBJC_FLAGS=\"$(gnustep-config --objc-flags | sed -Ee
's/-MMD //' -e 's/-E //' -e 's/-MP //')\"" >> /etc/bash.bashrc && \  
printf "\n%s\n" "export OBJC_FLAGS=\"$(gnustep-config --objc-flags | sed -Ee
's/-MMD //' -e 's/-E //' -e 's/-MP //')\"" >> /etc/profile && \  
printf "\n%s\n" "export BASE_LIBS=\"$(gnustep-config --base-libs)\"" >>
/etc/bash.bashrc && \  
printf "\n%s\n" "export BASE_LIBS=\"$(gnustep-config --base-libs)\"" >>
/etc/profile && \  
rm /gnustep-make-${GNUSTEP_MAKE_VERSION}.tar.gz && \  
rm /gnustep-base-${GNUSTEP_BASE_VERSION}.tar.gz && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD image-common /tmp/dexec/image-common  
VOLUME /tmp/dexec/build  
ENTRYPOINT ["bash", "-l", "/tmp/dexec/image-common/dexec-c-family.sh", "gcc
${OBJC_FLAGS} ${BASE_LIBS}"]  

