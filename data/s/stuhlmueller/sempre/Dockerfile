FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y software-properties-common python-software-properties
git ruby bzip2 make  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN apt-get install -y oracle-java7-installer  
RUN git clone https://github.com/percyliang/sempre.git /root/sempre  
RUN cd /root/sempre/ && ./download-dependencies core  
RUN cd /root/sempre && make

