FROM ubuntu:16.04  
MAINTAINER Vinicius Dias <viniciusvdias@dcc.ufmg.br>  
  
ENV STAND_HOME /usr/local/stand  
ENV STAND_CONFIG $STAND_HOME/conf/stand-config.yaml  
  
RUN apt-get update && apt-get install -y \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR $STAND_HOME  
COPY requirements.txt $STAND_HOM  
RUN pip install -r $STAND_HOME/requirements.txt  
  
COPY . $STAND_HOME  
RUN pybabel compile -d $STAND_HOME/stand/i18n/locales  
  
CMD ["/usr/local/stand/sbin/stand-daemon.sh", "startf"]  

