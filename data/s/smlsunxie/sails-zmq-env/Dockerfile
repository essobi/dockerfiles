FROM smlsunxie/sails-env:latest  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-
common python python-software-properties build-essential wget  
  
RUN wget http://download.zeromq.org/zeromq-4.0.4.tar.gz  
RUN tar zxvf zeromq-4.0.4.tar.gz && cd zeromq-4.0.4 && ./configure && make &&
make install  
RUN ldconfig  
RUN rm -rf /zeromq-4.0.4*  
  
RUN npm install -g zmq  
  
# Removed unnecessary packages  
RUN apt-get autoremove -y  
  
# Clear package repository cache  
RUN apt-get clean all  

