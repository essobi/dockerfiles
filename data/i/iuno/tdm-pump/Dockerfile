FROM gcc:latest  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get install -y \  
libboost-all-dev  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
COPY pumpcontrol.settings.conf /root  
  
RUN make ENCRYPTION=off REALDRIVERS=off  
  
CMD cd build && ./pumpcontrol.out --driver=simulation  
  
EXPOSE 9002  

