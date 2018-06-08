FROM mustardgrain/python:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get install -y g++  
RUN pip install locustio pyzmq  
  
COPY . /src  
  
RUN mkdir -p /etc/service/locust && cp /src/run /etc/service/locust  
  
EXPOSE 8089  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

