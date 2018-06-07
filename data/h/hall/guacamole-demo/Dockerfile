### Dockerfile for guacamole-demo based on hall\guacamole  
### This is a simple (but disk heavy) demo of guacamole. You  
### will be able to login to this container via an vncserver  
### running inside the container.  
### Only start this demo on a secure network. The passwords are  
### hardcoded and known to all. Build this yourself and be sure  
### to change the passwords in the following locations.  
### passwd - VNC password file. Password is demodemo  
### user-mapping.xml - Guacamole config. User: demo Pass:demo  
FROM hall/guacamole  
MAINTAINER Randy Hall <randy.hall@open-source.guru>  
  
### Install a full desktop in the container  
RUN apt-get update &&\  
apt-get -y install tightvncserver firefox xfce4  
  
### Install the vncpassword file and ssh keys  
RUN mkdir -p /root/.vnc && chmod 700 /root/.vnc  
ADD passwd /root/.vnc/passwd  
ADD xstartup /root/.vnc/xstartup  
RUN chmod 600 /root/.vnc/passwd &&\  
chmod a+x /root/.vnc/xstartup  
  
### Install the guacamole config  
ADD guacamole.properties /etc/guacamole/guacamole.properties  
ADD user-mappings.xml /etc/guacamole/user-mappings.xml  
  
### replace startup script so that vncserver is started  
RUN mkdir -p /etc/vncserver  
ADD vncservers.conf /etc/vncserver/vncservers.conf  
ADD vncserver /etc/init.d/vncserver  
ADD rc.local /etc/rc.local  
RUN chmod a+x /etc/rc.local && \  
chmod a+x /etc/init.d/vncserver  
  
### END  
# Launch with: docker run -d -v -p 8080:8080 guacamole-demo  
# Connect to http://your_host:8080  
# username: demo  
# password: demo  

