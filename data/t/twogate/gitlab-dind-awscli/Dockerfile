FROM gitlab/dind  
  
RUN apt-get install python2.7 \  
&& curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python2.7 get-pip.py \  
&& pip install awscli \  
&& rm -rf /var/lib/apt/lists/*  

