FROM bigtruedata/sbt  
  
RUN mkdir /sbt  
RUN cd /sbt && git clone https://github.com/glae/clean-duplicated-files.git
cdf  
WORKDIR /sbt/cdf  
  
RUN sbt compile  
ENTRYPOINT ["sbt"]

