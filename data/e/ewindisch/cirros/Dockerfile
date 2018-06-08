FROM scratch  
MAINTAINER Eric Windisch <ewindisch@docker.com>  
ADD cirros-0.3.3-x86_64-lxc.tar.gz /  
  
# Don't configure network  
RUN rm /etc/rc3.d/S40-network  
RUN sed -i '/is_lxc && lxc_netdown/d' /etc/init.d/rc.sysinit  
CMD ["/sbin/init"]  

