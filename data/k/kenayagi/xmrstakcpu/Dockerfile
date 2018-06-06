FROM ubuntu:16.04  
# Prepare directories  
RUN mkdir /config  
  
# Install dependencies  
RUN apt-get update && apt-get -y install libmicrohttpd-dev libssl-dev cmake
build-essential libhwloc-dev nano  
  
# Clean  
RUN rm -rf /var/lib/apt/lists/*  
  
# Get Code  
ADD https://github.com/fireice-uk/xmr-stak-cpu/archive/v1.3.0-1.5.0.tar.gz
/opt/xmr-stak-cpu.tar.gz  
RUN mkdir /opt/xmr-stak-cpu  
RUN tar xfv /opt/xmr-stak-cpu.tar.gz --strip 1 -C /opt/xmr-stak-cpu  
RUN sed -i 's/fDevDonationLevel = 2.0/fDevDonationLevel = 0.0/' /opt/xmr-stak-
cpu/donate-level.h  
WORKDIR /opt/xmr-stak-cpu  
RUN cmake .  
RUN make  
  
# Volume  
VOLUME /config  
ADD https://raw.githubusercontent.com/kenayagi/docker-
xmrstakcpu/master/config.txt /config/config.txt  
  
# Ports  
EXPOSE 8080  
# Command  
CMD ["/opt/xmr-stak-cpu/bin/xmr-stak-cpu", "/config/config.txt"]  

