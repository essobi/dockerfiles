FROM cypress/browsers:chrome65-ff57  
  
RUN echo "deb http://ftp.de.debian.org/debian testing main" >>
/etc/apt/sources.list \  
&& apt-get update && apt-get install -y --no-install-recommends \  
libc6-dev \  
python3.6 \  
python3-pip \  
python3-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install awscli  
  
CMD ["/bin/sh"]  
  

