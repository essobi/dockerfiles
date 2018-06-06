FROM ubuntu:latest  
MAINTAINER SYA-KE  
  
RUN apt-get -y update && apt-get -y install gcc build-essential wget libssl-
dev john  
RUN wget http://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.gz  
RUN rm `which john`  
RUN tar xzvf john-1.8.0-jumbo-1.tar.gz  
RUN cd john-1.8.0-jumbo-1/src && ./configure && make  
ENV PATH /john-1.8.0-jumbo-1/run:$PATH  
ADD ./john.ini /john.ini  
ADD ./john.local.conf /john.local.conf  
  
VOLUME ./john $HOME/.john  
VOLUME ./wordlist /wordlist  
  
ENTRYPOINT ["/bin/bash"]  

