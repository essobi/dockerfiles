FROM python:latest  
  
LABEL maintainer=""  
#ENV ZIP=SPAdes-3.11.1-Linux.tar.gz  
#ENV URL=http://cab.spbu.ru/files/release3.11.1  
#ENV FOLDER=SPAdes-3.11.1-Linux  
#ENV DST=/scripts  
  
RUN mkdir -p /scripts /data && \  
cd /scripts && \  
wget -q http://cab.spbu.ru/files/release3.11.1/SPAdes-3.11.1-Linux.tar.gz -O
/scripts/SPAdes-3.11.1-Linux.tar.gz && \  
tar xvf /scripts/SPAdes-3.11.1-Linux.tar.gz -C /scripts && \  
rm /scripts/SPAdes-3.11.1-Linux.tar.gz && \  
cd /usr/bin && \  
mv /scripts/SPAdes-3.11.1-Linux/bin/* . && \  
rm -rf /scripts/SPAdes-3.11.1-Linux  
  
# CHANGE WORKDIR TO /DATA  
WORKDIR /data  
  
# DEFINE DEFAULT COMMAND  
CMD ["bash"]  
  

