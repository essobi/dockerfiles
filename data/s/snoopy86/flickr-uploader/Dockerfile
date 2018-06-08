# Set base os  
FROM phusion/baseimage:0.9.16  
# Set correct environment variables  
ENV DEBIAN_FRONTEND=noninteractive HOME="/root" TERM=xterm LANG=en_US.UTF-8
LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
  
# Set volume  
VOLUME /photos  
VOLUME /folders2flickr  
  
# Set the locale  
RUN locale-gen en_US.UTF-8 && \  
# Fix a Debianism of the nobody's uid being 65534  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
# Install python  
apt-get update && \  
apt-get -y --force-yes install python-pip python-dev build-essential && \  
pip install --upgrade pip && \  
pip install --upgrade virtualenv && \  
apt-get -y --force-yes install git && \  
# Set start file  
curl -o /etc/my_init.d/uploadr.py
https://raw.githubusercontent.com/snoopy86/flickr-uploader/master/uploadr.py
&& \  
chmod +x /etc/my_init.d/uploadr.py && \  
# Clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true ))  

