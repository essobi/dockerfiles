FROM golang:1.8  
MAINTAINER an1sor0poUs "bad-hombres"  
RUN apt-get update  
  
RUN mkdir /root/work  
ENV GOPATH /root/work  
  
# Download Seclists --- /usr/share/seclists  
WORKDIR /usr/share/  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN curl -L https://github.com/danielmiessler/SecLists/archive/master.zip >
seclists.zip  
RUN unzip seclists.zip  
RUN cp -r SecLists-master/ seclists/ && rm seclists.zip  
VOLUME /usr/share/seclists  
  
WORKDIR /root/work  
RUN git clone https://github.com/dzonerzy/goWAPT.git  
  
# Install goWAPT  
WORKDIR /root/work/goWAPT/  
RUN make && make install  
  
COPY entrypoint.sh .  
ENTRYPOINT ["./entrypoint.sh"]  

