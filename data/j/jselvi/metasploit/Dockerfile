# This Docker image is based on the remnux/metasploit docker image, but
including a  
# framework and operating system update each time that it is build.  
#  
# Most lines below are copied from the remnux/metasploit Dockerfile.  
#  
# This Docker image file encapsulates Metasploit Framework, which is
distributed  
# from https://github.com/rapid7/metasploit-framework  
#  
# To run this image after installing Docker, use a command like this:  
#  
# sudo docker run --rm -it -p 443:443 -v ~/.msf4:/root/.msf4 -v
/tmp/msf:/tmp/data jselvi/metasploit  
#  
# The -p parameter exposes the ports on which you expect to receive inbound
connections from  
# reverse shells and such. Once the app starts, run the desired Metasploit
command, such as  
# "msfconsole" inside its container.  
#  
# After running the image, you'll have files from your Metasploit session in
the ~/.msf4 and  
# /tmp/msf directories on your host. The next time you run the app, it will
pick up from where  
# it left off by reading the files in those locations. If you wish to start
from scratch,  
# remove those directories ("sudo rm -rf ~/.msf4 /tmp/msf").  
#  
# In addition to including Metasploit Framework, the image also includes Nmap
and tmux.  
#  
FROM remnux/metasploit  
MAINTAINER Jose Selvi <jselvi@pentester.es>  
  
WORKDIR /opt  
USER root  
  
# Update operating system  
RUN apt-get update && apt-get -y dist-upgrade  
  
# Update Metasploit Framwork  
COPY update.sh /usr/local/bin/update.sh  
RUN sync  
RUN chmod a+xr /usr/local/bin/update.sh  
RUN /usr/local/bin/update.sh  
  
# Upload new init script, without update  
COPY init.sh /usr/local/bin/init.sh  
RUN sync  
RUN chmod a+xr /usr/local/bin/init.sh  
  
# Settings and custom scripts folder  
VOLUME /root/.msf4/  
VOLUME /tmp/data/  
  
# Starting script (DB + updates)  
CMD /usr/local/bin/init.sh  

