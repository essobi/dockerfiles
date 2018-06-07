FROM java:8  
  
ENV GROOVY_VERSION=2.4.5  
  
RUN wget -q --no-iri
https://bintray.com/artifact/download/groovy/maven/apache-groovy-
binary-${GROOVY_VERSION}.zip -O groovy.zip && unzip -q -d /opt/ groovy.zip &&
rm -rf groovy.zip && mv /opt/groovy-*/ /opt/groovy/  

