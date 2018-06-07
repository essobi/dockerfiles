FROM maven:3.5-jdk-8 as maven  
COPY tester /opt/hunnor-dict/export-ant/tester  
COPY formats /opt/hunnor-dict/export-ant/formats  
WORKDIR /opt/hunnor-dict/export-ant/tester  
RUN mvn  
  
FROM openjdk:8-jdk  
RUN mkdir /opt/export-ant  
RUN apt-get update && apt-get install --assume-yes --allow-unauthenticated ant
fop stardict-tools && apt-get clean  
ENV HUNNOR_ANT_JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV HUNNOR_ANT_SAXON_JAR /opt/saxon-9-he/saxon9he.jar  
ENV HUNNOR_ANT_STARDICT_COMPILER /usr/lib/stardict-tools/stardict-text2bin  
RUN mkdir -p /opt/saxon-9-he && \  
cd /opt/saxon-9-he && \  
wget -q https://downloads.sourceforge.net/project/saxon/Saxon-
HE/9.8/SaxonHE9-8-0-5J.zip && \  
unzip SaxonHE9-8-0-5J.zip && \  
rm -rf SaxonHE9-8-0-5J.zip doc notices saxon9-test.jar saxon9-xqj.jar  
COPY . /opt/export-ant  
WORKDIR /opt/export-ant  
ENTRYPOINT ["ant"]  

