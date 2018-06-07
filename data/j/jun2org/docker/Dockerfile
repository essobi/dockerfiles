FROM ubuntu:16.04  
  
# Install python3.6  
## Add python3.6 repository  
RUN apt-get update  
RUN apt-get install -y software-properties-common curl  
RUN add-apt-repository ppa:jonathonf/python-3.6  
RUN apt-get update  
  
## Install Essential package  
RUN apt-get install -y build-essential vim  
  
## Install python3.6  
RUN apt-get install -y python3.6 python3.6-dev  
  
## Install pip3.6  
RUN curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py"  
RUN python3.6 /tmp/get-pip.py  
  
## Setting language  
RUN apt-get install -y language-pack-ko  
  
RUN locale-gen ko_KR.UTF-8  
ENV LANG ko_KR.UTF-8  
ENV LANGUAGE ko_KR.UTF-8  
ENV LC_ALL ko_KR.UTF-8  
  
## Setting timezion  
ENV TZ Asia/Seoul  
  
RUN echo $TZ > /etc/timezone  
RUN apt-get install -y tzdata  
RUN rm /etc/localtime  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
## Clean up  
RUN apt-get remove -y software-properties-common curl \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  

