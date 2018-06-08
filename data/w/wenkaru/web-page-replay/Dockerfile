FROM ubuntu:trusty  
  
RUN apt-get update -y  
RUN apt-get install -y python  
  
COPY ./* /web-page-replay/  
COPY ./perftracker /web-page-replay/perftracker/  
COPY ./third_party /web-page-replay/third_party/  
COPY ./documentation /web-page-replay/documentation/  
  
WORKDIR /web-page-replay  
ENTRYPOINT ["./replay.py"]  

