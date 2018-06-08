FROM dgageot/busybox-ubuntu  
  
ENV MINOR_VERSION 79  
ENV BUILD_NUMBER b15  
  
# Need curl because built-in wget does not support https  
RUN (wget -O -
http://www.magicermine.com/demos/curl/curl/curl-7.30.0.ermine.tar.bz2 |
bunzip2 -c - | tar xf -) \  
&& mv /curl-7.30.0.ermine/curl.ermine /bin/curl \  
&& rm -Rf /curl-7.30.0.ermine  
  
RUN (curl -skLb "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/7u$MINOR_VERSION-$BUILD_NUMBER/jdk-7u$MINOR_VERSION-
linux-x64.tar.gz | tar xfz -) && \  
mv /jdk1.7.0_$MINOR_VERSION/jre /jre1.7.0_$MINOR_VERSION && \  
mv /jdk1.7.0_$MINOR_VERSION/lib/tools.jar /jre1.7.0_$MINOR_VERSION/lib/ext &&
\  
rm -Rf /jdk1.7.0_$MINOR_VERSION  
  
ENV JAVA_HOME /jre1.7.0_$MINOR_VERSION  
ENV PATH $PATH:$JAVA_HOME/bin  

