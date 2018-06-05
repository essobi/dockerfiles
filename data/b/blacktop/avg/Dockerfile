FROM debian:jessie  
MAINTAINER blacktop, https://github.com/blacktop  
  
# Make sure that Upstart won't try to start avgd after dpkg installs it  
# https://github.com/dotcloud/docker/issues/446  
ADD policy-rc.d /usr/sbin/policy-rc.d  
RUN /bin/chmod 755 /usr/sbin/policy-rc.d  
  
# Install Requirements  
RUN apt-get update -qq  
RUN apt-get install -qqy libc6-i386 supervisor  
  
# Get AVG Installer  
ADD http://download.avgfree.com/filedir/inst/avg2013flx-r3118-a6926.i386.deb
/avg/  
#ADD avg2013flx-r3118-a6926.i386.deb /avg/avg2013flx-r3118-a6926.i386.deb  
# Install AVG  
RUN dpkg -i /avg/avg2013flx-r3118-a6926.i386.deb  
  
# Start AVG Service and Update AVG Definitions  
RUN /etc/init.d/avgd restart && avgupdate  
RUN avgcfgctl -w UpdateVir.sched.Task.Disabled=true  
RUN avgcfgctl -w Default.setup.daemonize=false  
  
# Add Files  
ADD /supervisord-avg.conf /etc/supervisor/conf.d/supervisord-avg.conf  
ADD /malware/EICAR /malware/EICAR  
ADD /run.sh /run.sh  
RUN chmod 755 /*.sh  
  
WORKDIR /malware  
  
CMD ["/run.sh"]

