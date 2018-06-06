FROM python:3.6-stretch  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --no-cache-dir --upgrade pip \  
&& pip3 install --no-cache-dir boto3 pycurl  
  
COPY registry_view.py /usr/local/bin/registry_view.py  
  
RUN chmod +x /usr/local/bin/registry_view.py \  
&& python3 -OO -m compileall /usr/local/bin/registry_view.py  
  
ENTRYPOINT ["/usr/local/bin/python", "/usr/local/bin/registry_view.py"]  

