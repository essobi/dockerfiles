FROM ubuntu:16.04  
ENV REFRESHED_AT 27-FEB-2018  
RUN apt-get update  
RUN apt-get install -y python python3-pip build-essential libssl-dev libffi-
dev python3-dev git  
RUN pip3 install --upgrade pip  
  
WORKDIR /opt  
RUN git clone https://github.com/coursera-dl/coursera-dl  
WORKDIR /opt/coursera-dl  
RUN pip3 install -r requirements.txt  
  
RUN apt-get purge -y git  
RUN apt-get autoremove -y  
RUN apt-get clean  
  
RUN mkdir /root/workdir  
WORKDIR /root/workdir  
  
ENTRYPOINT ["/opt/coursera-dl/coursera-dl"]  
CMD ["--help"]  

