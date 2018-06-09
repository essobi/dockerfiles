FROM maven:3-jdk-8  
RUN git clone https://github.com/nla/outbackcdx.git && \  
cd outbackcdx && \  
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8 && \  
mvn package && \  
cp target/outbackcdx-*.jar ../outbackcdx.jar && \  
rm -fr outbackcdx  
  
RUN mkdir /cdx-data  
  
EXPOSE 8080  
CMD java -jar outbackcdx.jar -d /cdx-data -p 8080 -b 0.0.0.0  

