FROM debian:jessie  
MAINTAINER Andrzej Skrodzki  
  
ENV TERM linux  
RUN apt-get -y update  
  
RUN apt-get -y install gcc apache2-utils sysbench make openjdk-7-jdk
openjdk-7-jre  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
ADD logs/ /logs/  
ADD cpulimit/ /cpulimit/  
RUN make -C /cpulimit  
  
ADD xaa /xaa  
ADD xab /xab  
RUN cat /xaa /xab > /dacapo.jar  
  
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
ENV CPULIMIT 50  
CMD ["/run.sh"]  

