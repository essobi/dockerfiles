FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
python3 python3-pip libpq-dev \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN pip3 install --upgrade pip  
  

