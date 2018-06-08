FROM goabout/ansible  
  
MAINTAINER Go About <tech@goabout.com>  
  
RUN apt-get update -q && \  
apt-get install -yq python-pip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install dependencies  
RUN pip install backoff "boto<3"  
  
# Install serialization script  
COPY . /serialize/  
  
# Post-processing  
RUN mv /serialize/init-serialize.yml .  
  
# Default environment variable values  
ENV ANSIBLE_PROJECT ansible  
  
CMD ["sh", "/serialize/run.sh"]  

