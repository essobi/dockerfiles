#Name of container: docker-opensimulator  
#Version of container: 0.2.3  
FROM quantumobject/docker-baseimage:16.04  
MAINTAINER Murf  
  
#Add repository and update the container  
#Installation of necessary package/software for this containers...  
#nant was remove and added mono build dependence  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-get update && apt-get install -y -q screen mono-complete ca-
certificates-mono vim unzip \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
##Startup scripts  
#Pre-config scrip that needs to be run only when the container runs the first
time  
#Setting a flag for not running it again. This is used for setting up the
service.  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
##Adding Deamons to containers  
# To add opensim deamon to runit  
RUN mkdir /etc/service/opensim  
COPY opensim.sh /etc/service/opensim/unrun  
RUN chmod +x /etc/service/opensim/unrun  
  
#Pre-config script that needs to be run when container image is created  
#optionally include here additional software that needs to be installed or
configured for some service running on the container.  
COPY pre-conf.sh /sbin/pre-conf  
RUN chmod +x /sbin/pre-conf ; sync \  
&& /bin/bash -c /sbin/pre-conf \  
&& rm /sbin/pre-conf  
  
#Script to execute after install done and/or to create initial configuration  
COPY after_install.sh /sbin/after_install.sh  
RUN chmod +x /sbin/after_install.sh  
RUN chmod +x /opt/opensim/bin/opensim-ode.sh  
  
# To allow access from outside of the container to the container service at
these ports  
# Need to allow ports access rule at firewall too .  
EXPOSE 9000/tcp  
EXPOSE 9000/udp  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  

