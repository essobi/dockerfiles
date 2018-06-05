FROM phusion/baseimage:0.9.16  
MAINTAINER vwieczorek <vwieczorek@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
# Install scapy  
RUN apt-get update && \  
apt-get -qq -y install \  
gcc python-dev tcpdump graphviz imagemagick \  
swig python-crypto libpcap0.7 libpcap-dev python-scapy && \  
apt-get clean  
ADD https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py  
RUN python /tmp/get-pip.py  
RUN pip install -q numpy && \  
pip install --allow-all-external \  
PyX==0.12.1 pycrypto \  
\--allow-unverified gnuplot-py gnuplot-py  
  
# Install phue  
RUN pip install -q phue  
  
# dash-listen Configuration  
VOLUME /config  
  
RUN (crontab -l 2>/dev/null; echo "* * * * * /usr/bin/python /config/hue.py")
| crontab -  
RUN cron  
  
#CMD ["python", "/config/hue.py"]  
#CMD tail -f /var/log/syslog  

