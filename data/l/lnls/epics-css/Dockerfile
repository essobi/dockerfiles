FROM lnls/epics-base:debian-9.2  
  
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \  
apt-get update && \  
apt-get install -y \  
default-jre \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/epics/css && \  
cd /opt/epics/css && \  
curl -L -O https://github.com/lnls-sirius/lnls-
studio/releases/download/4.5.2/lnls-studio-4.5.2-SNAPSHOT-
linux.gtk.x86_64.tar.gz && \  
tar xvf lnls-studio-4.5.2-SNAPSHOT-linux.gtk.x86_64.tar.gz && \  
rm -rf lnls-studio-4.5.2-SNAPSHOT-linux.gtk.x86_64.tar.gz  

