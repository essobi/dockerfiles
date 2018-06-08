FROM debian:latest  
  
  
MAINTAINER Curt H. <curt@curtcreation.net>  
  
RUN dpkg --add-architecture i386  
RUN apt-get update && apt-get install -y wget unzip psmisc curl openssl ca-
certificates perl libtbb-dev \  
&& apt-get update \  
&& apt-get update \  
&& apt-get install -y libstdc++6 libgcc1 zlib1g libncurses5 \  
&& apt-get update \  
&& apt-get install -y lib32stdc++6 libtbb2:i386 lib32ncurses5 lib32z1 grep \  
&& adduser -D -h /home/container container  
  
USER container  
ENV USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./start.sh /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

