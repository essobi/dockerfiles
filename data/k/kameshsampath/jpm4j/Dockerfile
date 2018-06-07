FROM kameshsampath/openjdk8  
  
MAINTAINER Kamesh Sampath, kamesh.sampath@hotmail.com  
  
RUN curl -sL
https://github.com/jpm4j/jpm4j.installers/raw/master/dist/biz.aQute.jpm.run.jar
>jpm4j.jar && \  
java -jar jpm4j.jar -g init && \  
jpm install bnd  
  
CMD ["bnd","version"]

