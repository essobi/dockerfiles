FROM ubuntu:17.04  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y curl  
RUN apt-get install -y automake  
RUN apt-get install -y build-essential libtool  
RUN apt-get install -y gtk-doc-tools  
RUN apt-get install -y autopoint  
RUN apt-get install -y bison  
RUN apt-get install -y libxml2  
RUN apt-get install -y libxml2-dev  
RUN apt-get install -y libraptor2-0  
  
#install flex  
WORKDIR /  
RUN curl -L
https://github.com/westes/flex/releases/download/v2.6.3/flex-2.6.3.tar.gz >
flex.tar.gz  
RUN tar -xzvf flex.tar.gz  
WORKDIR flex-2.6.3  
RUN ./autogen.sh  
RUN ./configure && make && make install  
  
# CMD flex -h  
#install rapper  
WORKDIR /  
RUN git clone git://github.com/dajobe/raptor.git  
WORKDIR raptor  
RUN ./autogen.sh  
RUN make  
RUN make check  
RUN make install  
  
ENTRYPOINT ["rapper"]  

