FROM python:2.7  
RUN apt-get update && \  
apt-get install -y git libjudy-dev libarchive-dev pkg-config  
  
RUN mkdir -p /var/src/  
WORKDIR /var/src/  
  
RUN git clone https://github.com/traildb/traildb traildb  
  
WORKDIR /var/src/traildb  
  
RUN ./waf configure && ./waf build && ./waf install && tdb dump -i test  
  
RUN git clone https://github.com/traildb/traildb-python /var/src/traildb-
python  
  
WORKDIR /var/src/traildb-python  
  
RUN python setup.py install  
  
WORKDIR /var/src/traildb  
  
CMD ["bash"]  

