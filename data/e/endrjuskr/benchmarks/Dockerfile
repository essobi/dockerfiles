FROM debian:jessie  
MAINTAINER Andrzej Skrodzki  
  
ENV TERM linux  
RUN apt-get -y update  
  
RUN apt-get -y install apache2-utils sysbench openjdk-7-jdk openjdk-7-jre git
autoconf make gcc  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
ADD logs/ /logs/  
ADD xaa /xaa  
ADD xab /xab  
RUN cat /xaa /xab > /dacapo.jar  
  
RUN git clone https://github.com/endrjuskr/siege.git  
WORKDIR /siege  
RUN sh utils/bootstrap  
RUN sh configure --with-ssl=no  
RUN make  
RUN make install  
WORKDIR /  
  
ENV BENCH **null**  
ENV CL 5  
ENV NR 1000  
ENV COUNT 1  
ENV HOST http://localhost  
ENV WEBSITE index.html  
ENV PORT 3306  
ENV TIME 60  
ENV SIZE 50000  
ENV CMD **null**  
ENV THREADS 8  
ENV DELAY 1  
CMD ["/run.sh"]  

