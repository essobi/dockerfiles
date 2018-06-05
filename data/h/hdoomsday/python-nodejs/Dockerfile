FROM python:3.6  
RUN apt-get update \  
&& apt-get install -y sudo \  
&& apt-get install -y build-essential \  
&& apt-get install -y nodejs \  
&& apt-get install -y nodejs-legacy \  
&& apt-get install -y npm \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN useradd -m docker && \  
echo "docker:docker" | chpasswd && \  
echo "docker ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/docker && \  
chmod 0440 /etc/sudoers.d/docker  
  
USER docker  

