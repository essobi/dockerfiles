FROM python:2  
# Install dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends git libmpfr-
dev libssl-dev libmpc-dev libffi-dev build-essential libpython-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create a user account  
RUN adduser --disabled-password cowrie  
WORKDIR /home/cowrie/  
USER cowrie  
  
  
# Checkout the code  
RUN git clone http://github.com/micheloosterhof/cowrie  
WORKDIR /home/cowrie/cowrie  
USER root  
RUN pip install -r requirements.txt  
USER cowrie  
  
  
# Generate a DSA key  
RUN cd data && ssh-keygen -t dsa -b 1024 -f ssh_host_dsa_key  
  
# Install configuration file  
RUN cp cowrie.cfg.dist cowrie.cfg  
ADD userdb.txt data/userdb.txt  
  
# start  
EXPOSE 2222  
CMD cd data && ssh-keygen -t dsa -b 1024 -f ssh_host_dsa_key; cd ../ &&
./start.sh && tailf log/cowrie.log

