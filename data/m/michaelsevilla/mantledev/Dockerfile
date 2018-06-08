FROM ivotron/cephdev:latest  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
# install deps  
RUN apt-get update && \  
apt-get install -y lua5.2 liblua5.2-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /debian  
  
# create some startup scripts  
COPY standalone.sh /standalone.sh  
RUN chmod 750 /standalone.sh  
COPY greedy-spill.sh /greedy-spill.sh  
RUN chmod 750 /greedy-spill.sh  
ADD run.sh /run.sh  
  
# Add volumes for Ceph config and data  
VOLUME ["/etc/ceph","/var/lib/ceph"]  
  
# Expose the Ceph ports  
EXPOSE 6789 6800 6801 6802 6803 6804 6805 80 5000  

