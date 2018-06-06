FROM rugcompling/alpino:latest  
MAINTAINER Wouter van Atteveldt (wouter@vanatteveldt.com)  
EXPOSE 5002  
RUN apt-get -qq update && apt-get install -y python3-flask python3-pip
python3-lxml openjdk-7-jdk maven git  
  
# install NERC module # git checkout specific commit which is still 1.7,
debian:8 doesn not have java 8...  
RUN git clone https://github.com/ixa-ehu/ixa-pipe-nerc && (cd ixa-pipe-nerc &&
git checkout a86ce72f1de4b1aee18c9b20a89ea88ad9411d7c && mvn
-Dmaven.compiler.target=1.7 -Dmaven.compiler.source=1.7 clean package)  
  
# Get and unpack NERC models  
RUN curl http://i.amcat.nl/nerc-models-1.5.4-nl.tgz | tar xz  
RUN pip3 install alpinonaf>=0.4
git+https://github.com/vanatteveldt/coref_draft.git  
  
ENV NERC_MODEL=nerc-models-1.5.4/nl/nl-6-class-clusters-sonar.bin
NERC_JAR=ixa-pipe-nerc/target/ixa-pipe-nerc-1.6.1-exec.jar  
  
COPY alpinoserver.py .  
  
CMD python3 alpinoserver.py --host 0.0.0.0 --port 5002 --debug  

