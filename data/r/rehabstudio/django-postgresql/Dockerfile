FROM python:3.6  
RUN apt-get update && \  
apt-get install -y \  
postgresql \  
gettext && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install -U pip setuptools  
  
COPY requirements.txt /tmp  
RUN pip install --no-cache-dir -r /tmp/requirements.txt  

