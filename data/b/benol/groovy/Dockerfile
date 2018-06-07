FROM java:8  
ENV GROOVY_VERSION 2.3.7  
RUN curl -SLO http://dl.bintray.com/groovy/maven/groovy-
binary-$GROOVY_VERSION.zip  
RUN unzip /groovy-binary-$GROOVY_VERSION.zip -d /tmp \  
&& mv /tmp/groovy-$GROOVY_VERSION /groovy \  
&& rm /groovy-binary-$GROOVY_VERSION.zip  
  
ENV PATH /groovy/bin:$PATH  
WORKDIR /groovy  
  
CMD "groovysh"  

