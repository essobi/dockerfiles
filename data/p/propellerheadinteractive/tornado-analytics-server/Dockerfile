FROM ubuntu  
  
MAINTAINER Matt Kantor <matt@propellerhead.ca>  
  
RUN apt-get update -y && apt-get install git python python-pip -y  
RUN cd /tmp \  
&& git clone https://github.com/propellerhead-interactive/tornado-analytics-
server.git \  
&& cd tornado-analytics-server \  
&& pip install -r requirements.txt  
  
EXPOSE 8888  
CMD ["python", "/tmp/tornado-analytics-server/tserver.py"]

