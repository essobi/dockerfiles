FROM ubuntu:15.04  
RUN apt-get update \  
&& apt-get install -y \  
postgresql-common \  
libpq-dev \  
python-dev \  
python3-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /flexbot /flexbot/configuration /flexbot/flexbot /flexbot/samples
/flexbot/logs  
  
EXPOSE 80  
EXPOSE 8080  
COPY requirements.txt /flexbot/  
RUN pip3 install -r /flexbot/requirements.txt  
  
WORKDIR /flexbot  
  
CMD ["python3", "-m", "samples.run_flexbot", "--config",
"configuration/config.yaml", "--logging-config", "configuration/logging.yaml"]  
  
COPY samples /flexbot/samples  
COPY exercises /flexbot/exercises  
COPY flexbot /flexbot/flexbot  

