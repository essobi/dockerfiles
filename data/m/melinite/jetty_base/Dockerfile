# use with docker 1.4.1+ recommended  
# jetty 9 - I have been using jetty for years in production. Love it for its
utilitarian simplicity and performance.  
# http://download.eclipse.org/jetty/stable-9/dist/jetty-
distribution-9.2.10.v20150310.tar.gz  
FROM melinite/oracle-java8-jdk:latest  
MAINTAINER David Seong <melinite@gmail.com>  
  
  
# As always, define userspace; security is going to be an ongoing issue with
popularity of Docker.  
# Beware of privilege escalation and do not trust arbitrary docker files
blindly.  
USER root  
  
  
# If you use this as a base image, I HIGHLY recommend to use JETTY_BASE
directive in your new dockerfile  
# to keep your customizations separate from the binary distro.  
# Makes for very easy jetty upgrades without touching your app and
customizations. +1^.^ to jetty team for modules and base!  
# http://www.eclipse.org/jetty/documentation/current/startup-base-and-
home.html  
#  
ENV JETTY_VERSION=9.2.10.v20150310 \  
JETTY_HOME=/opt/jetty9  
# JETTY_BASE=/opt/myApp  
RUN wget http://download.eclipse.org/jetty/${JETTY_VERSION}/dist/jetty-
distribution-${JETTY_VERSION}.tar.gz -O /tmp/jetty.tar.gz && \  
cd /opt && tar xf /tmp/jetty.tar.gz && \  
ln -s /opt/jetty-distribution-${JETTY_VERSION} ${JETTY_HOME} && \  
rm -r ${JETTY_HOME}/demo-base && \  
rm /tmp/jetty.tar.gz  
  

