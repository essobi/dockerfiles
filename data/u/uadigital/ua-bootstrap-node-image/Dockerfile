FROM node:8.9.0-stretch  
  
RUN apt-get update \  
&& apt-get install -y \  
python-dev \  
python-pip \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install 'awscli~=1.11.171' \  
&& yarn global add gulp@'~3.9.1'  

