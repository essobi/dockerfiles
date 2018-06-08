FROM kalilinux/kali-linux-docker  
MAINTAINER SYA-KE  
  
RUN apt-get update && \  
apt-get -qq -y install \  
unzip python python-pyx \  
python-matplotlib tcpdump python-crypto \  
graphviz imagemagick gnuplot python-gnuplot \  
libpcap-dev && apt-get clean  
ADD https://github.com/secdev/scapy/archive/master.zip /tmp/master.zip  
RUN unzip /tmp/master.zip -d /usr/local/ && rm /tmp/master.zip  
ENV PYTHONPATH /usr/local/scapy-master  
WORKDIR $PYTHONPATH  
ENTRYPOINT ["python","-m","scapy.__init__"]  

