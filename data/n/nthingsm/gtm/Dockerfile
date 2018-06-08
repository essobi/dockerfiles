FROM ubuntu:latest  
ENV TZ 'America/Mexico_City'  
# Install git and wget  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y git wget tzdata &&\  
apt-get clean  
  
RUN echo $TZ > /etc/timezone && \  
rm /etc/localtime && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# Install gtm  
RUN wget https://github.com/git-time-
metric/gtm/releases/download/v1.2.11/gtm.v1.2.11.linux.tar.gz && \  
tar -zxvf gtm.v1.2.11.linux.tar.gz -C /usr/bin && \  
gtm --version

