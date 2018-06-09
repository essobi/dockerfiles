FROM ubuntu:latest  
  
RUN apt-get update -y -q  
RUN apt-get install -y -q build-essential  
RUN apt-get install -y -q ruby  
RUN apt-get install -y -q ruby-dev  
RUN apt-get install -y -q zlib1g-dev  
RUN apt-get install -y -q libasound-dev libpulse-dev libjpeg-dev libtiff-dev
libx11-6 libxext6 libpng12-0 libslang2 libsdl-image1.2  
RUN gem install rake roo  
COPY rakefile /root/rakefile  
COPY entry.sh /bin/entry.sh  
RUN mkdir -p /app && chmod +x /bin/entry.sh  
WORKDIR /app  
ENTRYPOINT ["/bin/entry.sh"]  

