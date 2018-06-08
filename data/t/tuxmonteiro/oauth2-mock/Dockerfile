FROM tuxmonteiro/scala-sbt:0.13.16  
MAINTAINER tuxmonteiro  
  
COPY . /opt  
  
WORKDIR /opt  
  
RUN /usr/bin/sbt update  
  
EXPOSE 9000  
CMD ["/usr/bin/sbt", "~run"]

