FROM varsy/centos6-utils  
  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
RUN yum install -y nrpe nagios-plugins-disk nagios-plugins-load nagios-
plugins-procs nagios-plugins-tcp nagios-plugins-mysql nagios-plugins-http  
RUN echo "command[check_disks]=/usr/lib64/nagios/plugins/check_disk -w 10% -c
5% -W 10% -K 5%" >> /etc/nrpe.d/check_disks.cfg  
  
ADD plugins/ /usr/lib64/nagios/plugins/  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh  
  
CMD /run-services.sh  
  
EXPOSE 5666  

