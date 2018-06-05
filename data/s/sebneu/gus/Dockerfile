FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y \  
software-properties-common  
RUN add-apt-repository universe  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
python-pip \  
libpq-dev \  
python-dev \  
python-tk \  
cron  
  
RUN pip install git+git://github.com/ADEQUATeDQ/GUS.git  
  
#ARG port=5000  
#ARG gitlab="http://data.adequate.at/"  
#ARG local-gitlab="http://data.adequate.at/"  
#EXPOSE $port  
#CMD ["gus", "--port", $port, "--gitlab", $gitlab, "--local-gitlab", $local-
gitlab]  
ENTRYPOINT ["/bin/bash", "-c", "gus ${*}", "--"]  

