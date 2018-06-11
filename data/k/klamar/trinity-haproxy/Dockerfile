FROM million12/haproxy:1.6.3-h2  
  
RUN set -ex \  
&& yum install -y python-pip \  
&& pip install requests  
  
ADD consul /consul  
  
ENTRYPOINT ["python", "/consul/run.py"]  

