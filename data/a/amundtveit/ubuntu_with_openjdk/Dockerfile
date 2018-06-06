FROM ubuntu:16.04  
RUN apt update -y  
RUN apt upgrade -y  
RUN apt install default-jdk mysql-client ca-certificates curl git unzip netcat
-y  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  
  

