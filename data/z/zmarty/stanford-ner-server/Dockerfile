# Version 1.0.0  
FROM ubuntu:15.04  
MAINTAINER Ovidiu Dan <contact@ovidiudan.com>  
  
RUN apt-get update && apt-get -y install \  
openjdk-8-jdk \  
openjdk-8-jre \  
unzip \  
wget  
  
WORKDIR /home  
RUN wget -O ner.zip http://nlp.stanford.edu/software/stanford-
ner-2015-04-20.zip  
RUN unzip ner.zip  
  
ENV port=9000 classifierPath=classifiers/english.muc.7class.distsim.crf.ser.gz
outputFormat=inlineXML  
  
EXPOSE $port  
  
WORKDIR /home/stanford-ner-2015-04-20  
CMD java -mx1000m -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer \  
-loadClassifier $classifierPath \  
-port $port -outputFormat $outputFormat  
  

