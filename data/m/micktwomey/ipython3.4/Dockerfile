FROM micktwomey/python3.4:latest  
MAINTAINER Michael Twomey, mick@twomeylee.name  
  
RUN pip3.4 install -U "numpy==1.9.2"  
RUN pip3.4 install -U "ipython[notebook]==3.2.1"  
RUN pip3.4 install -U "pandas==0.16.2"  
RUN apt-get -q -y install libpng12-dev libfreetype6-dev  
RUN pip3.4 install -U "matplotlib==1.4.3"  
  
ENTRYPOINT ["/usr/local/bin/ipython"]  

