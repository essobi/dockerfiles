FROM nginx:stable  
  
VOLUME /pictures  
  
WORKDIR /opt  
  
RUN apt-get update && apt-get install -y \  
python-dev \  
python-pip \  
zlib1g-dev \  
libjpeg-dev \  
libfreetype6-dev \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip install sigal  
  
COPY run.sh sigal.conf.py auth.conf auth.htpasswd ./  
  
ENV LANG C.UTF-8  
CMD ["./run.sh"]  

