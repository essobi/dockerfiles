FROM cdecker/bitcoin-dev:latest  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \  
apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer libxext-dev libxrender-dev libxtst-
dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ADD state.xml /tmp/state.xml  
  
RUN wget http://dlc-
cdn.sun.com/netbeans/8.0.1/final/bundles/netbeans-8.0.1-cpp-linux.sh -O
/tmp/netbeans.sh -q && \  
chmod +x /tmp/netbeans.sh && \  
echo 'Installing netbeans' && \  
/tmp/netbeans.sh --silent --state /tmp/state.xml && \  
rm -rf /tmp/*  
  
ADD run /usr/local/bin/netbeans  
RUN chmod +x /usr/local/bin/netbeans  
  
USER developer  
WORKDIR /bitcoin  
CMD /usr/local/bin/netbeans  
  

