FROM java:8  
MAINTAINER Tobi Schäfer <interface@p3k.org>  
  
# Although ADD seems nicer than RUN, it does not cache. Bummer!  
#ADD http://dev.orf.at/download/helma/1.7.0/helma-1.7.0.tar.gz /tmp/  
WORKDIR /tmp  
  
RUN curl -O http://dev.orf.at/download/helma/1.7.0/helma-1.7.0.tar.gz  
  
WORKDIR /root  
  
RUN tar -xzf /tmp/*.gz  
RUN rm -rf /tmp/*.gz  
  
WORKDIR /root/helma-1.7.0  
  
ENTRYPOINT ["/usr/bin/java", "-server", "-Xmx128m", "-jar",
"/root/helma-1.7.0/launcher.jar"]  
CMD ["-w", "8080"]  

