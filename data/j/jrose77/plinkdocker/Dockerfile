FROM ubuntu:xenial  
RUN apt-get update && apt-get install -y curl unzip && apt-get clean  
RUN curl 'https://www.cog-
genomics.org/static/bin/plink161010/plink_linux_x86_64.zip' > /tmp/plink.zip  
RUN cd /tmp && unzip plink.zip && rm plink.zip  
RUN mv /tmp/plink /usr/local/bin  

