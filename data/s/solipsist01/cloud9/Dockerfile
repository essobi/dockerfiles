FROM kdelfour/cloud9-docker  
  
RUN apt-get update \  
&& apt-get install -y python-setuptools python3-setuptools \  
&& easy_install pip \  
&& pip install requests youtube-dl flask  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  

