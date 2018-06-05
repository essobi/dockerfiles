#Download base image ubuntu 16.04  
FROM debian:jessie-slim  
  
RUN apt-get update  
RUN apt-get install -y git-core python3 python3-pip  
RUN pip3 install --upgrade pip  
RUN python3 -m pip install coinbase  
RUN python3 -m pip install git+https://github.com/alimcmaster1/gdax-
python@ff07566a0d381d8ee043e597f3adaf432eaae741  
  
COPY autosell.py /autosell.py  
  
CMD ["/usr/bin/python3", "/autosell.py"]  

