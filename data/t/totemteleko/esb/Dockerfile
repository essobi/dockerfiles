#  
# Clean ESB Dockerfile based on ServiceMix  
#  
# Pull base image.  
FROM totemteleko/servicemix  
MAINTAINER totemteleko totemteleko@gmail.com  
  
  
# Move configuration file.  
ADD collectd.conf /servicemix/  
ADD org.apache.karaf.features.cfg /servicemix/etc/  
ADD org.apache.servicemix.nmr.cfg /servicemix/etc/  
ADD org.apache.servicemix.jbi.cfg /servicemix/etc/  
ADD setenv /servicemix/bin/  
  
# Move run file.  
ADD esb.sh /servicemix/  
  
# Expose ports. SSH Port, ESB instance SSH port, collectd port.  
EXPOSE 22 8101 25826/udp  
  
# Initial command  
CMD /servicemix/esb.sh -mb  

