FROM sellpy/python3-jupyter-sklearn:latest  
  
ADD install.sh /tmp/install.sh  
RUN sh -e /tmp/install.sh  
  
RUN mkdir /app  
WORKDIR /app  
RUN git clone https://github.com/awslabs/amazon-kinesis-client-python.git  
WORKDIR /app/amazon-kinesis-client-python  
RUN python3 setup.py install  

