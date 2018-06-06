FROM committed/java  
MAINTAINER Committed Software <docker@committed.software>  
  
# Install the Java JCE Policy  
RUN curl -q -L -C - -b "oraclelicense=accept-securebackup-cookie" -o
/tmp/jce_policy-8.zip -O http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip \  
&& unzip -oj -d /usr/lib/jvm/java-8-oracle/jre/lib/security
/tmp/jce_policy-8.zip \\*/\\*.jar \  
&& rm /tmp/jce_policy-8.zip  
  

