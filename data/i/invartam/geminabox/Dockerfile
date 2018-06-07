FROM ubuntu:16.04  
RUN apt update  
RUN apt install -y ruby ruby-dev build-essential  
RUN gem install geminabox  
RUN mkdir -p /opt/geminabox  
  
ADD resources/opt/ /opt/  
ADD resources/bin/ /bin/  
  
RUN chmod 755 /bin/start.sh  
  
WORKDIR /opt/geminabox  
  
ENTRYPOINT [ "/bin/start.sh" ]  

