FROM phusion/baseimage:0.9.16  
MAINTAINER IronCore Labs  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
WORKDIR /root  
  
ENV CB_SERVER_VERSION "3.0.1"  
ENV CB_SERVER_FILE "couchbase-server-
enterprise_${CB_SERVER_VERSION}-ubuntu12.04_amd64.deb"  
ENV CB_SERVER_URL
"http://packages.couchbase.com/releases/${CB_SERVER_VERSION}/${CB_SERVER_FILE}"  
RUN apt-get update && apt-get install -y wget  
  
# Install just security updates  
RUN apt-get -s dist-upgrade | grep "^Inst" | grep -i securi | awk -F " "
{'print $2'} | xargs apt-get install  
  
# I do wget on its own RUN line and early in the file on purpose to reduce the
number of re-downloads while creating the file  
RUN wget "${CB_SERVER_URL}"  
RUN dpkg -i ${CB_SERVER_FILE} && rm ${CB_SERVER_FILE}  
  
RUN mkdir -p /etc/service/couchbase-server  
COPY scripts/couchbase-start /etc/service/couchbase-server/run  
  
COPY scripts/setup.sh /usr/local/bin/couchbase-setup.sh  
  
EXPOSE 8091 8092 8093 11207 11210 11211 18091 18092  
VOLUME /opt/couchbase/var  

