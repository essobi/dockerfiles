FROM hokiegeek/scala-sbt:latest  
  
RUN git clone https://github.com/HokieGeek/catacombs.git /tmp/catacombs  
WORKDIR /tmp/catacombs  
  
RUN echo 'git pull origin master && sbt run $@' > /usr/bin/catacombs-run  
  
ENTRYPOINT ["/bin/sh", "/usr/bin/catacombs-run"]  

