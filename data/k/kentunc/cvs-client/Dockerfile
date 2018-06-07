FROM debian:latest  
  
RUN apt-get update && apt-get install -y cvs \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CVSROOT /root/cvs  
WORKDIR $CVSROOT  

