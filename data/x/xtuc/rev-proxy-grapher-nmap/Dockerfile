FROM python:3.6-stretch  
  
ENV WORKDIR /usr/app  
  
WORKDIR $WORKDIR  
  
RUN apt-get update  
RUN apt-get install -y git nmap graphviz  
  
RUN pip3 install pydotplus PyYAML netaddr python-nmap  
  
RUN git clone https://github.com/mricon/rev-proxy-grapher.git  
  
COPY entrypoint.sh .  
RUN chmod +x entrypoint.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  

