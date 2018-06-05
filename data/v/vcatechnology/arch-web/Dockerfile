FROM vcatechnology/arch-ci:latest  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="An up-to-date Arch Linux image with packages for
browser testing" \  
org.label-schema.url="https://www.archlinux.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-arch-web" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
  
# Install packages necessary for unit testing browsers  
RUN sudo vca-install-package \  
npm \  
chromium \  
firefox \  
xorg-server-xvfb \  
x11vnc \  
nodejs \  
jre8-openjdk \  
gcc \  
gconf \  
openssh \  
yarn  
  
ENV LAUNCHPAD_CHROME /usr/local/bin/chromium-no-sandbox  
  
ENV CHROME_BIN /usr/local/bin/chromium-no-sandbox  
  
ENV CHROMIUM_BIN /usr/local/bin/chromium-no-sandbox  
  
RUN sudo su -c " \  
echo '#! /bin/sh' > /usr/local/bin/chromium-no-sandbox && \  
echo 'chromium \$@ --no-sandbox' >> /usr/local/bin/chromium-no-sandbox && \  
chmod +x /usr/local/bin/chromium-no-sandbox && \  
exit"  

