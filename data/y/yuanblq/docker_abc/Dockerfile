FROM jenkins  
  
MAINTAINER Yuan "744421791@qq.com"  
USER root  
  
RUN rm -f /etc/apt/sources.list  
ADD ./dev_tools/aliyun-sources-debian9.list /etc/apt/sources.list  
#RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 40976EAF437D05B5
&& apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 3B4FE6ACC0B21F32  
RUN apt-get update  
RUN apt-get update --fix-missing  
RUN apt-get install -y vim python3-pip git  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt install -y npm  
RUN npm install -g hexo-cli  
  
RUN mkdir /workspace  
ADD ./dev_tools/requirements.txt /workspace  
WORKDIR /workspace  
RUN pip3 install -r requirements.txt  
RUN npm install -g newman  
  
USER jenkins  

