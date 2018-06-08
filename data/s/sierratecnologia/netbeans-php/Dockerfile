FROM sierratecnologia/java:8  
MAINTAINER Ricardo Sierra "sierra.csi@gmail.com"  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \  
apt-get update && apt-get install -y software-properties-common libxext-dev
libxrender-dev libxtst-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ADD state.xml /tmp/state.xml  
  
RUN wget
http://download.netbeans.org/netbeans/8.1/final/bundles/netbeans-8.1-php-
linux-x64.sh -O /tmp/netbeans.sh -q && \  
chmod +x /tmp/netbeans.sh && \  
echo 'Installing netbeans' && \  
/tmp/netbeans.sh --silent --state /tmp/state.xml && \  
rm -rf /tmp/*  
  
ADD run /usr/local/bin/netbeans  
  
RUN chmod +x /usr/local/bin/netbeans && \  
mkdir -p /home/root/.netbeans  
  
ENV HOME /home/root  
WORKDIR /home/root  
CMD /usr/local/bin/netbeans  

