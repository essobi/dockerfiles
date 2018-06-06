FROM python:latest  
  
RUN apt-get -y update && apt-get install -y \  
curl \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& cd ~ && git clone -b development
https://aeternas@bitbucket.org/aeternas/casas-master.git \  
&& chmod +x ~/casas-master/master.py  
  
CMD ~/casas-master/master.py  

