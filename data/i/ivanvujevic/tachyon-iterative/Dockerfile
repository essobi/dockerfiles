FROM ubuntu  
MAINTAINER Ivan Vujević <ivan.vujevic92@gmail.com>  
  
RUN apt-get update && apt-get install make && apt-get -y install g++  
  
RUN mkdir -p /Tachyon  
COPY ./ /Tachyon/  
  
WORKDIR /Tachyon  
  
RUN make  

