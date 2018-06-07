FROM ubuntu:14.04  
  
MAINTAINER Stig Tore Aannoe <staannoe@gmail.com>  
  
RUN apt-get update -y  
  
# Force -y for apt-get  
#######################  
RUN echo "APT::Get::Assume-Yes true;" >>/etc/apt/apt.conf  
  
RUN apt-get install curl unzip git make python-pip && apt-get clean  
  
  
# Add app  
##################  
WORKDIR /  
RUN git clone https://github.com/mailpile/Mailpile.git  
WORKDIR /Mailpile  
RUN git checkout release/beta  
# Build app  
###########  
RUN make debian-dev && apt-get clean  
RUN ./mp setup  
  
  
# Add dockerize startup script  
##############################  
RUN apt-get install -y wget  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-
amd64-v0.0.2.tar.gz  
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.2.tar.gz  
RUN chmod +x /usr/local/bin/dockerize  
  
  
VOLUME ["/root/.local/share/Mailpile"]  
  
EXPOSE 33411  
  
CMD "dockerize" "/Mailpile/mp" "--www=0.0.0.0:33411" "--wait"  

