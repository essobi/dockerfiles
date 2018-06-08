FROM openjdk:alpine  
  
# Update and install dependencies  
RUN apk update  
RUN apk add apache-ant  
RUN apk add git  
  
# Clone the repository and switch to branch for JIoT  
RUN git clone https://github.com/stefanopiozingaro/jolie.git jolie-git  
WORKDIR /jolie-git  
RUN git checkout next  
  
# Install Jolie with ant and set JOLIE_HOME  
RUN ant dist-install  
ENV JOLIE_HOME /usr/local/lib/jolie  
  
# Clean up  
WORKDIR /home  
RUN rm -rf /jolie-git  

