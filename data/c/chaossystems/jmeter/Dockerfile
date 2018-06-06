FROM openjdk:9  
ARG JMETER_VER=4.0  
WORKDIR /jmeter  
  
RUN curl -LsO http://artfiles.org/apache.org/jmeter/binaries/apache-
jmeter-$JMETER_VER.tgz && \  
tar zxvf apache-jmeter-$JMETER_VER.tgz && \  
mv apache-jmeter-$JMETER_VER/* . && \  
rm -rf apache-jmeter-$JMETER_VER*  
  
# Expose the default server port.  
EXPOSE 8000  
#================================================================================  
#Don't use GUI mode for load testing !, only for Test creation and Test
debugging.  
#For load testing, use NON GUI Mode:  
# jmeter -n -t [jmx file] -l [results file] -e -o [Path to web report folder]  
#& increase Java Heap to meet your test requirements:  
# Modify current env variable HEAP="-Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m"
in the jmeter batch file  
#Check : https://jmeter.apache.org/usermanual/best-practices.html  
#================================================================================  
ENTRYPOINT ["/jmeter/bin/jmeter"]  
CMD ["-n", "-t"]  

