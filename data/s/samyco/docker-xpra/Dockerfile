# This Dockerfile builds an image with which you can remotely control any
application using xpra  
FROM samyco/docker-xpra:debian-stretch  
  
MAINTAINER Samy Coenen "contact@samycoenen.be"  
RUN apt-get install -y \  
wget \  
openjdk-8-jdk \  
icedtea-plugin && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
#firefox  
RUN wget https://download-
installer.cdn.mozilla.net/pub/firefox/releases/52.6.0esr/linux-x86_64/en-
GB/firefox-52.6.0esr.tar.bz2 && tar -xjf firefox-52.6.0esr.tar.bz2 && mv
firefox /opt/firefox52 && ln -s /opt/firefox52/firefox /usr/bin/firefox  
  
# Add user  
RUN adduser --disabled-password --gecos "User" \--uid 1000 $XPRA_USER  
  
USER $XPRA_USER  
  
EXPOSE 14500  
CMD rm -f /tmp/.X100-lock && XPRA_PASSWORD=$(tr -dc _A-Z-a-z-0-9 <
/dev/urandom | head -c 8) && echo "xpra password is: "$XPRA_PASSWORD && xpra
start $DISPLAY \--tcp-auth=password:value=$XPRA_PASSWORD \--bind-
tcp=0.0.0.0:14500 --start='firefox' && sleep infinity

