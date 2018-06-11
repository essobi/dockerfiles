FROM java:8  
ENV JYTHON_VERSION 2.7.0  
RUN apt-get update && apt-get install -y curl && apt-get clean  
  
RUN curl -L "http://search.maven.org/remotecontent?filepath=org/python/jython-
installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar" -o
jython_installer-${JYTHON_VERSION}.jar  
  
RUN java -jar jython_installer-${JYTHON_VERSION}.jar -s -d
$HOME/jython-${JYTHON_VERSION} -i ensurepip  
  
RUN ln -s $HOME/jython-${JYTHON_VERSION}/bin/jython /usr/bin  
  
RUN rm jython_installer-${JYTHON_VERSION}.jar  
  
CMD ["jython"]  

