FROM python:2  
MAINTAINER layolu <layolulayole@gmail.com>  
  
WORKDIR /  
RUN apt-get -q update \  
&& apt-get -qy install git-core \  
&& git clone https://github.com/slackhq/python-rtmbot.git \  
&& cd python-rtmbot \  
&& pip install -r requirements.txt \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD run-rtmbot.sh /  
  
CMD sh /run-rtmbot.sh  

