FROM cypress/base:8  
  
RUN apt-get update \  
&& apt-get install -y jshon python-pip python-dev \  
&& pip install awscli \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD bin /usr/local/bin  

