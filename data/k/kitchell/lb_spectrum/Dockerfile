  
FROM neurodebian:nd16.04  
MAINTAINER Lindsey Kitchell <kitchell@indiana.edu>  
  
RUN apt update && \  
apt install -y git python-vtk python-numpy python-scipy  
  
RUN git clone https://github.com/nipy/mindboggle.git /mindboggle && \  
cd /mindboggle && python setup.py install  
COPY main.py /main.py  
  
RUN mkdir /output && ldconfig  
  
WORKDIR /output  
ENTRYPOINT ["/main.py"]  
  

