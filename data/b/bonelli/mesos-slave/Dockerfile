############################################################  
# Dockerfile to run Mesos Slaves  
# Based on Ubuntu Image  
############################################################  
# Set the base image to use to Ubuntu  
FROM itzg/ubuntu-openjdk-7  
# Set the file maintainer (your name - the file's author)  
MAINTAINER Federico Bonelli  
  
RUN apt-get update  
  
RUN apt-get install -y python-setuptools python-protobuf curl  
  
# install mesos from mesosphere  
RUN curl -sSfL
http://downloads.mesosphere.io/master/ubuntu/14.04/mesos_0.19.0~ubuntu14.04%2B1_amd64.deb
--output /tmp/mesos.deb  
RUN dpkg -i /tmp/mesos.deb  
RUN rm /tmp/mesos.deb  
  
# install python egg  
RUN curl -sSfL
http://downloads.mesosphere.io/master/ubuntu/14.04/mesos-0.19.0_rc2-py2.7-linux-x86_64.egg
--output /tmp/mesos.egg  
RUN easy_install /tmp/mesos.egg  
RUN rm /tmp/mesos.egg  
  
# set up mesos a bit  
RUN echo -n "manual" > /etc/init/mesos-master.override  
  
RUN echo "LOGS=/var/log/mesos" > /etc/default/mesos  
RUN echo "PORT=5051" > /etc/default/mesos-slave  
  
# install R  
RUN cd /tmp  
RUN apt-get install -y r-recommended r-cran-rcurl libc6  
# this ugly part is because r-cran-rjava depends on the complete jre, but the
headless is installed already, so we don't need the complete which doesn't
install on docker because of fuse  
RUN cd /tmp && apt-get download r-cran-rjava  
RUN dpkg --force-all -i /tmp/r-cran-rjava*.deb  
RUN rm /tmp/r-cran-rjava*.deb  
RUN curl -sSfL https://github.com/bonelli/SparkR-pkg/tarball/master --output
/tmp/sparkR-master.tgz  
RUN tar xvf /tmp/sparkR-master.tgz -C /tmp  
RUN mv /tmp/bonelli-SparkR-pkg* /tmp/SparkR-pkg  
RUN cd /tmp/SparkR-pkg && LD_LIBRARY_PATH="/usr/lib/jvm/java-7-openjdk-
amd64/jre/lib/amd64/server" ./install-dev.sh  
  
ENV LD_LIBRARY_PATH /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server  
#RUN rm -fR /tmp/sparkR-master.tgz  
EXPOSE 5051  
# Default run command arguments  
CMD echo "$MESOS_PASSWD" >> /etc/passwd && /usr/bin/mesos-init-wrapper slave
--master "$MESOS_MASTER"  
  
USER root  
  

