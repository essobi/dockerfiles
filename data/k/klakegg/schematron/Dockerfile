FROM maven:3.5.0-jdk-8 AS mvn  
  
ADD . $MAVEN_HOME/project  
  
RUN cd $MAVEN_HOME/project \  
&& mvn -B clean package \  
&& folder=$(ls $MAVEN_HOME/project/target | grep "full" | head -1) \  
&& mv $MAVEN_HOME/project/target/$folder/schematron /schematron  
  
FROM java:8-jre-alpine  
  
COPY \--from=mvn /schematron /schematron  
  
VOLUME /src  
  
WORKDIR /src  
  
ENTRYPOINT ["sh", "/schematron/bin/run.sh"]

