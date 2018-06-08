FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -qy git python python-setuptools ca-certificates wget
--no-install-recommends  
RUN git clone https://github.com/mumrah/kafka-python  
  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install requests  
  
WORKDIR kafka-python  
  
RUN python setup.py install  
  
WORKDIR /  
  
RUN git clone https://github.com/nqn/nibbler.git  
  
WORKDIR nibbler  

