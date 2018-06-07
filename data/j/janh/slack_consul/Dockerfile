FROM ubuntu:14.04  
RUN mkdir -p /data  
COPY . /data  
WORKDIR /data  
  
RUN apt-get update && apt-get install git python python-dev python3
python3-dev python3-pip python-pip build-essential -y && apt-get clean  
RUN pip3 install -e .  
  
CMD ["slack_consul"]  

