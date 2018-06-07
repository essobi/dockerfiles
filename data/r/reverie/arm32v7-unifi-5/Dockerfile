FROM resin/rpi-raspbian:jessie  
MAINTAINER Guto Andreollo <gutoandreollo@users.noreply.github.com>  
  
# This image uses cross-build to build on x86_64 hosts. See details on  
# https://resin.io/blog/building-arm-containers-on-any-x86-machine-even-
dockerhub/  
RUN [ "cross-build-start" ]  
  
# UniFi doesn't really work with openjdk, even on an RPi3. The performance is
just not up to par.  
RUN apt-get update && apt-get install -y oracle-java8-jdk && rm -rf
/var/lib/apt/lists/*  
  
# steps adapted from:  
# https://help.ubnt.com/hc/en-us/articles/220066768-UniFi-How-to-Install-
Update-via-APT-on-Debian-or-Ubuntu  
# Add the unifi repository, add the private key and update it.  
RUN echo 'deb http://www.ubnt.com/downloads/unifi/debian unifi5 ubiquiti' >>
/etc/apt/sources.list.d/ubnt.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && \  
apt-get update && \  
apt-get install --no-install-recommends -y -q --force-yes unifi && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# We don't need to start mongodb, UniFi will do that for it's own instance  
RUN echo 'ENABLE_MONGODB=no' | tee -a /etc/mongodb.conf > /dev/null  
  
RUN [ "cross-build-end" ]  
  
# Five directories at all, although most remain empty?  
VOLUME ["/var/lib/unifi", "/var/log/unifi", "/var/run/unifi",
"/usr/lib/unifi/work", "/usr/lib/unifi/data"]  
  
# All the different ports for different purposes...  
EXPOSE 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 3478/udp  
  
WORKDIR /var/lib/unifi  
  
CMD ["/usr/bin/java", "-Xmx768M", "-jar", "/usr/lib/unifi/lib/ace.jar",
"start"]  

