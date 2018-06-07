FROM ubuntu:14.04  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
RUN apt-get update -y -q  
  
RUN echo "APT::Get::Assume-Yes true;" >>/etc/apt/apt.conf  
  
RUN apt-get install -y -qq curl unzip git make python-pip wget && apt-get
clean -y -qq  
  
WORKDIR /  
RUN git clone https://das-repo.de/web/Mailpile.git  
WORKDIR /Mailpile  
RUN git checkout stable  
  
RUN make debian-dev && apt-get clean  
RUN ./mp setup  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-
amd64-v0.0.2.tar.gz  
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.2.tar.gz  
RUN chmod +x /usr/local/bin/dockerize  
  
VOLUME ["/root/.local/share/Mailpile"]  
  
EXPOSE 33411  
CMD "dockerize" "/Mailpile/mp" "--www=0.0.0.0:33411" "--wait"

