FROM alpine:3.5  
RUN apk add --no-cache shadow sudo git build-base util-linux  
  
RUN useradd -m meltdown && \  
echo 'meltdown:nwodtlem' | chpasswd  
RUN echo 'meltdown ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
USER meltdown  
  
RUN cd $HOME\  
&& git clone https://github.com/IAIK/meltdown \  
&& cd meltdown \  
&& make  

