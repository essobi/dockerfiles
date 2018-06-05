FROM openshift/base-centos7  
MAINTAINER "Patrick Double <pat@patdouble.com>"  
ARG BUILD_DATE  
ARG SOURCE_COMMIT  
ARG DOCKERFILE_PATH  
ARG SOURCE_TYPE  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="$DOCKERFILE_PATH/Dockerfile" \  
org.label-schema.license="GPLv2" \  
org.label-schema.name="OpenShift S2I base builder image including headless
browsers for functional testing" \  
org.label-schema.url="https://bitbucket.org/double16/openshift-s2i-browser-
base" \  
org.label-schema.vcs-ref=$SOURCE_COMMIT \  
org.label-schema.vcs-type="$SOURCE_TYPE" \  
org.label-schema.vcs-
url="https://bitbucket.org/double16/openshift-s2i-browser-base.git"  
  
USER root  
  
# Some proxies will get in the way here, so increasing to avoid time out
errors  
RUN echo "timeout=200" >> /etc/yum.conf  
# gtk3 required for firefox  
RUN yum install -y xorg-x11-server-Xvfb.x86_64 gtk3 fontconfig bzip2 && yum
clean all -y  
  
ENV FIREFOX_VERSION=50.1.0 PHANTOMJS_VERSION=2.1.1
CHROME_VERSION=stable_current TERM=dumb  
  
# PhantomJS  
RUN curl --silent --show-error --location --fail --retry 3
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2
| tar xjfO - phantomjs-${PHANTOMJS_VERSION}-linux-x86_64/bin/phantomjs >
/usr/bin/phantomjs && chmod +x /usr/bin/phantomjs  
  
# Google Chrome  
RUN curl --silent --show-error --location --fail --retry 3
https://dl.google.com/linux/direct/google-chrome-${CHROME_VERSION}_x86_64.rpm
> /tmp/google-chrome-${CHROME_VERSION}_x86_64.rpm && yum install -y
/tmp/google-chrome-${CHROME_VERSION}_x86_64.rpm && rm /tmp/google-
chrome-${CHROME_VERSION}_x86_64.rpm && yum clean all -y  
  
# Firefox  
RUN curl --silent --show-error --location --fail --retry 3
http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/en-
US/firefox-${FIREFOX_VERSION}.tar.bz2 >
/tmp/firefox-${FIREFOX_VERSION}.tar.bz2 && mkdir
/opt/firefox-${FIREFOX_VERSION} && tar xjf
/tmp/firefox-${FIREFOX_VERSION}.tar.bz2 -C /opt/firefox-${FIREFOX_VERSION} &&
rm /tmp/firefox-${FIREFOX_VERSION}.tar.bz2  
  
RUN echo 'exec xvfb-run -d -s "-screen 0
${SCREEN_WIDTH}x${SCREEN_HEIGHT}x${SCREEN_DEPTH} -ac +extension RANDR"
/opt/firefox-${FIREFOX_VERSION}/firefox/firefox "$@"' > /usr/bin/firefox &&
chmod +x /usr/bin/firefox  
  
RUN mv /opt/google/chrome/google-chrome /opt/google/chrome/google-chrome.orig
&& echo 'exec xvfb-run -a -s "-screen 0
${SCREEN_WIDTH}x${SCREEN_HEIGHT}x${SCREEN_DEPTH} -ac +extension RANDR"
/opt/google/chrome/google-chrome.orig --no-sandbox "$@"' >
/opt/google/chrome/google-chrome && chmod +x /opt/google/chrome/google-chrome  
  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null TERM=dumb SCREEN_WIDTH=1360
SCREEN_HEIGHT=1020 SCREEN_DEPTH=24  
ADD test /opt/image-test/test  
ADD Makefile image-test.sh /opt/image-test/  
  

