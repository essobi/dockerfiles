FROM ubuntu:latest  
  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install -y build-essential libssl-dev wget  
  
WORKDIR /usr/local/src  
RUN wget -O - http://download.joedog.org/siege/siege-latest.tar.gz | tar xzvf
-  
  
WORKDIR /usr/local/src/siege-4.0.4  
RUN ./configure --with-ssl=/usr/bin/openssl && make && make install  
  
WORKDIR /  
COPY siege.sh siege.sh  
RUN chmod a+x siege.sh  
  
CMD ["./siege.sh"]  

