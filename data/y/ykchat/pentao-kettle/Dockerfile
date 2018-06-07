FROM ubuntu:trusty  
  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java8-installer  
RUN apt-get -y install unzip  
RUN apt-get clean  
  
RUN mkdir /usr/src/pentaho  
WORKDIR /usr/src/pentaho  
RUN wget --progress=dot:giga
http://downloads.sourceforge.net/project/pentaho/Data%20Integration/6.0/pdi-
ce-6.0.1.0-386.zip  
RUN unzip pdi-ce-6.0.1.0-386.zip  
RUN rm pdi-ce-6.0.1.0-386.zip  
  
WORKDIR data-integration  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
EXPOSE 8080  
ENTRYPOINT ["./carte.sh", "0.0.0.0", "8080"]  
CMD []  

