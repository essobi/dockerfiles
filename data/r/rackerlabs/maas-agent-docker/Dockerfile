FROM phusion/baseimage:0.9.11  
CMD ["/sbin/my_init"]  
  
# disable ssh  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# install agent  
RUN curl -o meta.deb
http://meta.packages.cloudmonitoring.rackspace.com/ubuntu-14.04-x86_64/rackspace-
cloud-monitoring-meta-stable_1.0_all.deb && \  
dpkg -i meta.deb && \  
apt-get -y update && \  
apt-get install -y rackspace-monitoring-agent && \  
rm -f meta.deb && \  
mkdir /etc/service/rackspace-monitoring-agent  
  
ADD rackspace-monitoring-agent.sh /etc/service/rackspace-monitoring-agent/run  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

