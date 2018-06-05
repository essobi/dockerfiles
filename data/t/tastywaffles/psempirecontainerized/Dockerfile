# Usage:  
#  
# How to build  
# docker build -t <stuff> .  
#  
# How to run this  
# docker run -it -p 192.168.1.25:8080:8080 -v /tmp:/tmp empire  
FROM ubuntu:16.04  
LABEL maintainer="dastardly0x90@gmail.com"  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
python \  
lsb-release  
  
RUN git clone https://github.com/EmpireProject/Empire.git  
#Generates staging key for database  
ENV STAGING_KEY=RANDOM  
  
EXPOSE 8080  
WORKDIR /Empire  
#Installs Empire  
RUN bash -c "./setup/install.sh" \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["./empire"]  

