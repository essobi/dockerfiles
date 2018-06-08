FROM gcc:7  
MAINTAINER Michail "cs16mtech11009@iith.ac.in"  
RUN mkdir /home/chatapp/  
  
COPY chatserver.c /home/chatapp/.  
WORKDIR /home/chatapp/  
  
RUN gcc -pthread -o chatserver chatserver.c  
  
EXPOSE 5000  
WORKDIR /home/chatapp/  
CMD ["./chatserver", "5000"]  

