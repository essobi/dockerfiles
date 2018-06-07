# How to build: sudo docker build -t nano_cast .  
# How to run (local build): sudo docker run -d -p 8888:8888 nano_cast  
# How to run (dockerhub): sudo docker run -d -p 8888:8888 nanowallet/nano_cast  
FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
python3-dev \  
python3-pip \  
&& pip3 install --upgrade pip  
  
RUN pip3 install \  
tornado \  
requests \  
dataset  
  
ADD . / nano_cast/  
  
EXPOSE 8888  
ENV RAI_NODE_URI="127.0.0.1" \  
RAI_NODE_PORT="7076"  
WORKDIR nano_cast  
  
ENTRYPOINT python3 run.py \  
\--rai_node_uri=${RAI_NODE_URI} \  
\--rai_node_port=${RAI_NODE_PORT}  

