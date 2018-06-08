FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y qt5-default build-essential wget curl
npm  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN mkdir -p /var/script/PacketSender  
WORKDIR /var/script/PacketSender  
RUN wget https://github.com/dannagle/PacketSender/archive/v5.3.1.tar.gz  
RUN tar -xzvf v5.3.1.tar.gz  
WORKDIR /var/script/PacketSender/PacketSender-5.3.1/src  
RUN qmake  
RUN make  
RUN chmod a+x PacketSender  
RUN cp PacketSender /usr/local/bin/packetsender  

