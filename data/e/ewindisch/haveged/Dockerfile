FROM debian:latest  
RUN apt-get update; apt-get install -qy haveged  
ENTRYPOINT ["haveged"]  
CMD ["-F1"]  

