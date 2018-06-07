FROM continuumio/anaconda3  
  
RUN apt update && \  
apt install -y openssh-server \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install tushare

