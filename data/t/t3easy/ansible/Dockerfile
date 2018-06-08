FROM python:2.7  
  
RUN apt-get update && apt-get install -y \  
openssh-client \  
&& rm -r /var/lib/apt/lists/*  
  
RUN pip install ansible --no-cache-dir  

