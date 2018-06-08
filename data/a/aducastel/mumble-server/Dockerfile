FROM ubuntu:16.04  
  
RUN apt update && \  
DEBIAN_FRONTEND=noninteractive apt install -y \  
python-software-properties \  
software-properties-common \  
sudo \  
&& add-apt-repository ppa:mumble/release \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv 5E6DA83306132997 \  
&& apt-add-repository "deb http://zeroc.com/download/apt/ubuntu`lsb_release
-rs` stable main" \  
&& apt update \  
&& DEBIAN_FRONTEND=noninteractive apt install -y \  
busybox-syslogd \  
mumble-server \  
&& apt-get clean \  
&& mkdir /data  
  
ADD start.sh /start.sh  
  
CMD ["/start.sh"]  

