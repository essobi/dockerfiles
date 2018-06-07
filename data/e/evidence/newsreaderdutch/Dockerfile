FROM rugcompling/alpino:latest  
MAINTAINER Martine de Vos (mgdevos@gmail.com)  
  
# Ubuntu dependencies  
RUN apt-get update -qq && apt-get install -y wget lsof sed git  
  
# Java dependencies  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update -qq \  
&& apt install -t jessie-backports -y openjdk-8-jdk ca-certificates-java \  
&& /usr/sbin/update-java-alternatives -s java-1.8.0-openjdk-amd64 \  
&& apt-get install -y maven  
  
# Python dependencies  
RUN apt-get install -y python-pip python-lxml \  
&& pip install KafNafParserPy alpinonaf future  
  
# Tilburg ILK dependencies  
RUN apt-get install -y timbl  
  
# VUA-CLTL dependencies  
RUN mkdir central-dependencies \  
&& cd central-dependencies \  
&& git clone https://github.com/cltl/vua-resources  
  
# Download dbpedia-spotlight servers  
RUN cd central-dependencies \  
&& mkdir dbpedia-spotlight \  
&& cd dbpedia-spotlight \  
&& wget https://downloads.dbpedia-spotlight.org/spotlight/dbpedia-
spotlight-0.7.1.jar \  
&& wget https://downloads.dbpedia-spotlight.org/2016-10/nl/model/nl.tar.gz \  
&& tar -xzvf nl.tar.gz \  
&& mvn install:install-file -Dfile=dbpedia-spotlight-0.7.1.jar -DgroupId=ixa
-DartifactId=dbpedia-spotlight -Dversion=0.7 -Dpackaging=jar
-DgeneratePom=true \  
&& rm nl.tar.gz  
  
# Install and compile tokenizer; use specific version (not necessarily latest)  
RUN git clone https://github.com/ixa-ehu/ixa-pipe-tok \  
&& cd ixa-pipe-tok \  
&& git checkout 739ff20 \  
&& mvn clean install  
  
# Download ixa-pipes package to get matching ixa-pipe-nerc jar and model
versions  
RUN wget http://ixa2.si.ehu.es/ixa-pipes/models/ixa-pipes-1.1.1.tar.gz \  
&& mkdir ixa-pipe-nerc \  
&& tar -zxvf ixa-pipes-1.1.1.tar.gz ixa-pipes-1.1.1/ixa-pipe-
nerc-1.6.1-exec.jar \  
&& tar -xzvf ixa-pipes-1.1.1.tar.gz ixa-pipes-1.1.1/nerc-
models-1.6.1/nl/nl-6-class-clusters-sonar.bin \  
&& mv ixa-pipes-1.1.1/ixa-pipe-nerc-1.6.1-exec.jar ixa-pipe-nerc/ \  
&& mv ixa-pipes-1.1.1/nerc-models-1.6.1/nl/nl-6-class-clusters-sonar.bin ixa-
pipe-nerc/ \  
&& rm ixa-pipes-1.1.1.tar.gz \  
&& rm -Rf ixa-pipes-1.1.1  
  
# Download and install ixa-pipe-ned  
RUN git clone https://github.com/ixa-ehu/ixa-pipe-ned \  
&& cd ixa-pipe-ned \  
&& git checkout 062a983 \  
&& mvn -Dmaven.compiler.target=1.7 -Dmaven.compiler.source=1.7 clean package  
  
# Download and install svm_wsd  
RUN git clone https://github.com/cltl/svm_wsd.git \  
&& cd svm_wsd \  
&& git checkout 0300439 \  
&& ./install_naf.sh  
  
# Download and install ixa-heideltime  
RUN git clone https://github.com/ixa-ehu/ixa-heideltime \  
&& cd ixa-heideltime \  
&& wget http://goo.gl/D6lUEN \  
&& tar -xzvf D6lUEN \  
&& mv heideltime-standalone/de.unihd.dbs.heideltime.standalone.jar ./lib \  
&& mv heideltime-standalone/config.props . \  
&& rm D6lUEN \  
&& rm -R heideltime-standalone \  
&& wget http://ixa2.si.ehu.es/%7Ejibalari/jvntextpro-2.0.jar \  
&& mv jvntextpro-2.0.jar lib/ \  
&& wget https://github.com/carchrae/install-to-project-
repo/raw/master/install-to-project-repo.py \  
&& python2 install-to-project-repo.py \  
&& mvn clean install  
  
# Download and install ontological tagger  
RUN git clone https://github.com/cltl/OntoTagger \  
&& cd OntoTagger \  
&& git checkout c3796c5 \  
&& mvn clean install  
  
# Download semantic role labeler  
RUN git clone https://github.com/newsreader/vua-srl-nl \  
&& cd vua-srl-nl \  
&& git checkout 997a85f \  
&& sed -i 's/set -e//' run.sh  
  
# Download additional roles  
RUN git clone https://github.com/newsreader/vua-srl-dutch-nominal-events \  
&& cd vua-srl-dutch-nominal-events \  
&& git checkout 6115b31  
  
# Download EventCoreference  
RUN git clone https://github.com/cltl/EventCoreference.git \  
&& cd EventCoreference \  
&& git checkout a346edd \  
&& sed -i '46s| <version>v3.1.2</version>| <version>master-
SNAPSHOT</version>|' pom.xml \  
&& mvn clean install \  
&& mkdir lib \  
&& mv ./target/EventCoreference-v*-jar-with-dependencies.jar ./lib/  
  
# Download and install opinion_miner_deluxePP  
RUN git clone https://github.com/rubenIzquierdo/opinion_miner_deluxePP.git \  
&& cd opinion_miner_deluxePP \  
&& git checkout 40a714c  
  
# Download the central-dependency installation checker  
RUN wget https://github.com/ADAH-
EviDENce/NewsReader/raw/master/NewsReaderDutch/check_dependencies.sh \  
&& chmod o+x check_dependencies.sh \  
&& ./check_dependencies.sh  
  
# Download main bash script  
RUN wget https://github.com/ADAH-
EviDENce/NewsReader/raw/master/NewsReaderDutch/newsreader.sh \  
&& chmod a+x newsreader.sh  
  
# This ENTRYPOINT overrides the CMD in the Alpino Docker  
# User still has to specify the path to inputfile(s)  
ENTRYPOINT ["/newsreader.sh"]  
# CMD ["/bin/bash"]  

