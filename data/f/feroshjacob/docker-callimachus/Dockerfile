FROM ubuntu:14.04  
MAINTAINER Nolan Nichols <nolan.nichols@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y openjdk-7-jdk wget unzip  
  
WORKDIR /home  
RUN wget https://github.com/3-Round-
Stones/callimachus/releases/download/v1.5.1/callimachus-1.5.1.zip  
RUN unzip callimachus-1.5.1.zip  
RUN rm callimachus-1.5.1.zip  
  
ADD callimachus.conf /home/etc/callimachus.conf  
  
RUN /home/bin/callimachus-setup.sh  
RUN /home/bin/callimachus-stop.sh  
  
ENTRYPOINT ["/home/bin/callimachus.sh"]  
  
# Visit this URL to set username and password  
#
http://192.168.99.100:8080/?register&token=c7a7fc9f4e89b6cf65ad1c0e841fe11a&nonce=2c5705c2&email=root%40f5ee59d47428  

