FROM debian:wheezy  
  
ADD https://bootstrap.pypa.io/get-pip.py /get-pip.py  
RUN apt-get update && apt-get install -y \  
build-essential \  
python-dev \  
git \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN chmod +x /get-pip.py  
RUN /get-pip.py  
RUN mkdir /fm  
WORKDIR /fm  
COPY . /fm  
  
RUN python setup.py install  
  
CMD fm-slack  

