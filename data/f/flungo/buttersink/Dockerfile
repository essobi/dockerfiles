FROM python:2  
RUN apt-get update  
RUN apt-get install -y btrfs-tools  
RUN pip install buttersink  
  
ADD buttersinkstrap /usr/local/bin/buttersinkstrap  
  
ENTRYPOINT ["buttersinkstrap"]  
  
VOLUME ["/root/.boto"]  
  
WORKDIR /pwd  

