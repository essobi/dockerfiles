FROM ubuntu:14.04  
  
# Set the root password to something I know  
RUN echo "root:rootpassword" | chpasswd  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y octave qtoctave  
  
# Switch to a non-root user  
RUN useradd -ms /bin/bash ubuntu  
  
USER ubuntu  
WORKDIR /home/ubuntu  
  
CMD qtoctave  

