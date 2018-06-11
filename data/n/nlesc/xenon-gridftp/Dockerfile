# Docker container with gridftp server, to run the xenon gridftp adaptor
integration tests against.  
#  
# Build with:  
#  
# docker build -t nlesc/xenon-gridftp .  
#  
# Run with:  
#  
#  
FROM nlesc/xenon-phusion-base  
MAINTAINER Jason Maassen "j.maassen@esciencecenter.nl"  
# Use the globus from the package manager:  
#  
RUN apt-get update && apt-get install -y libglobus-ftp-client2 \  
libglobus-gridftp-server-control0 globus-gridftp-server-progs \  
globus-gss-assist-progs && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
# Alternatively, we can install the latest globus using:  
#  
# RUN apt-get update && apt-get install -y wget && \  
# wget
http://downloads.globus.org/toolkit/gt6/stable/installers/repo/deb/globus-
toolkit-repo_latest_all.deb && \  
# dpkg -i globus-toolkit-repo_latest_all.deb && \  
# rm globus-toolkit-repo_latest_all.deb && \  
# apt-get install -f && \  
# apt-get update && \  
# apt-get install -y globus-connect-server && \  
# apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
# install ca certificates  
mkdir /etc/ca-files  
ADD files /etc/ca-files  
RUN dpkg -i /etc/ca-files/globus-simple-ca-*_all.deb  
  
# create user mapping  
ADD map_users.sh /usr/bin/  
ADD map_user.sh /usr/bin/  
RUN /usr/bin/map_users.sh  
  
# init script which setups host certificates and starts gridftp server  
RUN mkdir -p /etc/service/gridftp  
ADD gridftp.sh /etc/service/gridftp/run  
ADD gridftp.conf /etc/gridftp.conf  
  
EXPOSE 2811  
EXPOSE 50000-51000  
CMD ["/sbin/my_init"]  

