FROM renyufu/esp32-idf  
  
RUN apt-get install -y python-pip python-dev build-essential libssl-dev  
RUN pip install git+https://github.com/renyufu/restexec.git  
  
VOLUME /esp  
WORKDIR /proj  
  
ENTRYPOINT ["restexec"]  

