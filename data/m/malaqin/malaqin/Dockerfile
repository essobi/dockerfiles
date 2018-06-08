FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y wget  
RUN apt-get install -y ruby  
  
RUN ruby --version  
  
RUN wget https://github.com/busyloop/lolcat/archive/master.zip && \  
unzip master.zip  
RUN cd lolcat-master/bin && gem install lolcat  
WORKDIR /lolcat-master/bin  
  
CMD ["-h"]  
ENTRYPOINT ["lolcat","-f"]  

