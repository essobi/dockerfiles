FROM ubuntu:16.04  
WORKDIR /app  
  
COPY requirements.txt /app  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update \  
&& apt-get -y install build-essential python3 python3-dev python3-pip libffi-
dev python3-numpy python3-scipy libssl-dev libev4 libev-dev \  
&& pip3 install --upgrade pip \  
&& pip3 install --no-cache-dir -v -r requirements.txt \  
&& apt-get -y remove build-essential \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY . /app  
RUN python3 setup.py install  
  
CMD ["python3", "worker"]

