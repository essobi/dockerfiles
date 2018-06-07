# Used https://github.com/gawbul/docker-sge as inspiration/source  
FROM nlesc/xenon-phusion-base  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
  
RUN echo "Package: xserver-xorg*\nPin: release *\nPin-Priority: -1" >>
/etc/apt/preferences && \  
echo "Package: unity*\nPin: release *\nPin-Priority: -1" >>
/etc/apt/preferences && \  
echo "Package: gnome*\nPin: release *\nPin-Priority: -1" >>
/etc/apt/preferences && \  
echo "gridengine-master shared/gridenginemaster string $HOSTNAME" | debconf-
set-selections && \  
echo "postfix postfix/main_mailer_type string 'No configuration'" | debconf-
set-selections && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y gridengine-master
gridengine-exec gridengine-client inotify-tools && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose sshd port  
EXPOSE 22  
# Expose ge qmaster  
EXPOSE 6444  
# Expose ge execd  
EXPOSE 6445  
# add init scripts for master and exec deamons  
RUN mkdir -p /etc/my_init.d  
ADD etc/my_init.d/gridengine.sh /etc/my_init.d/gridengine.sh  
  
# config  
ADD etc/gridengine /etc/gridengine/files  
WORKDIR /etc/gridengine/files  
RUN mkdir host_groups exec_hosts && \  
# Ignore domains  
perl -pi -e 's/false/true/' /var/lib/gridengine/default/common/bootstrap && \  
echo $HOSTNAME > /var/lib/gridengine/default/common/act_qmaster && \  
/etc/init.d/gridengine-master start && sleep 2 && \  
# submit host  
qconf -as $HOSTNAME && \  
# hosts for queues  
/bin/echo -e "group_name @allhosts\nhostlist $HOSTNAME" > host_groups/allhosts
&& \  
qconf -Ahgrp host_groups/allhosts && \  
qconf -Ap parallel_environments/bi && \  
qconf -Ap parallel_environments/fillup && \  
qconf -Ap parallel_environments/round && \  
qconf -Ap parallel_environments/smp && \  
qconf -Aq queues/default && \  
qconf -Aq queues/slow && \  
qconf -Msconf scheduler && \  
qconf -Mconf configurations/global && \  
killall sge_qmaster  
  
CMD ["/sbin/my_init"]  
  
# Check that qmaster, execd and sshd deamons accept connections  
HEALTHCHECK --interval=1s CMD qping -info $(hostname) 6444 qmaster 1 && \  
qping -info $(hostname) 6445 execd 1 && \  
ssh -o NoHostAuthenticationForLocalhost=yes -i /home/xenon/.ssh/id_rsa
xenon@localhost /bin/true || \  
exit 1  

