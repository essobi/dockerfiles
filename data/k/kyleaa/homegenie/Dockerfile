FROM phusion/baseimage  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
run apt-get update && apt-get install -y gdebi-core && apt-get clean -y  
add homegenie-beta_1.00.r482_all.deb /tmp/  
run gdebi --non-interactive /tmp/homegenie-beta_1.00.r482_all.deb  
run mkdir /etc/service/homegenie  
add homegenie.runit /etc/service/homegenie/run  
  
# cleanup  
run rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

