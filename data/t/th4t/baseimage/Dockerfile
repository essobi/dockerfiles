# based on https://github.com/phusion/baseimage-docker  
FROM phusion/baseimage:0.9.16  
MAINTAINER Vladislav Supalov <mail@th4t.net>  
ENV REFRESHED_AT 2015-01-25  
# set correct environment variables  
ENV HOME /root  
# disable SSH, this is not really necessary in the newest baseimage anymore  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# the custom init process  
ENTRYPOINT ["/sbin/my_init"]  
  
# -- starts all runit services, and executes the next command  
# -l makes the bash to be invoked as a login shell  
CMD ["--" ,"bash", "-l"]  

