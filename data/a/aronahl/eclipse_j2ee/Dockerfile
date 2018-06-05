FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND=noninteractive  
ADD ["getUrl.py", "runit.py", "/usr/local/bin/"]  
WORKDIR /opt  
RUN apt-get update && \  
apt-get upgrade -fy && \  
apt-get install -fy python3-pip \  
software-properties-common \  
curl \  
libwebkitgtk-3.0-0 \  
openjdk-8-jdk \  
openjdk-8-source \  
software-properties-common \  
greybird-gtk-theme && \  
pip3 install bs4 dumb-init && \  
/usr/local/bin/getUrl.py | tar -xzv && \  
curl http://winswitch.org/gpg.asc | apt-key add \- && \  
echo "deb http://winswitch.org/ xenial main" >
/etc/apt/sources.list.d/winswitch.list && \  
add-apt-repository universe && \  
apt-get update && \  
apt-get install -fy xpra && \  
adduser user && \  
mkdir /opt/workspace && \  
chown -R user /opt/eclipse /opt/workspace && \  
apt-get remove -y python3-pip curl && \  
apt-get autoclean -y && \  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
groupadd -g 999 docker && \  
usermod -aG 999 user  
USER user  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "/usr/local/bin/runit.py" ]  
CMD [ ]  

