FROM sellpy/python3-jupyter-sklearn:latest  
  
ADD install.sh /tmp/install.sh  
RUN sh -e /tmp/install.sh  
  
ADD requirements.txt /tmp/requirements.txt  
RUN pip3 install -r /tmp/requirements.txt  
  
RUN mkdir /app  
WORKDIR /app  

