FROM jallegri/ubuntustudio-audio-base  
  
MAINTAINER Jonatan Allegrini <jallegri@gmail.com>  
  
RUN \  
apt-get update && \  
printf no\n | apt-get install -y audacity --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["audacity"]  

