FROM suzlab/python:latest  
  
RUN pip install locustio pyzmq  
  
WORKDIR /root  
  
COPY .bashrc.patch ./  
RUN patch .bashrc < .bashrc.patch  
RUN rm .bashrc.patch  

