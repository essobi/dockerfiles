FROM java:openjdk-7-jdk  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
RUN git clone https://github.com/systemslab/baseball-consistency.git  
ENV CLASSPATH /baseball-consistency/bin  
  
# override tutum's run.sh with our own  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
ENTRYPOINT ["/run.sh"]  

