# mminderbinder/letsencrypt  
FROM mminderbinder/baseimage  
MAINTAINER Milo Minderbinder <minderbinder.enterprises@gmail.com>  
  
RUN apt-get update && apt-get -y install \  
python2.7 \  
python-dev \  
git  
  
ADD https://bootstrap.pypa.io/get-pip.py get-pip.py  
RUN python get-pip.py  
  
RUN git clone https://github.com/letsencrypt/letsencrypt /root/letsencrypt  
# Run letsencrypt client's automatic installer/configurator  
RUN sh /root/letsencrypt/letsencrypt-auto --help  
  
RUN pip install letsencrypt-s3front  
  
COPY run-letsencrypt.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run-letsencrypt.sh  
  
# Clean up APT when done  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init", "--", "/usr/local/bin/run-letsencrypt.sh"]  
  

