FROM ubuntu:16.04  
MAINTAINER Vinicius Dias <viniciusvdias@dcc.ufmg.br>  
  
ENV TAHITI_HOME /usr/local/tahiti  
ENV TAHITI_CONFIG $TAHITI_HOME/conf/tahiti-config.yaml  
  
RUN apt-get update && apt-get install -y \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR $TAHITI_HOME  
COPY requirements.txt $TAHITI_HOME/requirements.txt  
RUN pip install -r $TAHITI_HOME/requirements.txt  
  
COPY . $TAHITI_HOME  
  
CMD ["/usr/local/tahiti/sbin/tahiti-daemon.sh", "startf"]  

