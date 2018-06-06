FROM mebitech/oracle-java:8u144  
  
RUN cd /tmp/ && \  
curl -LO "http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip" -H
'Cookie: oraclelicense=accept-securebackup-cookie' && \  
unzip jce_policy-8.zip && \  
rm jce_policy-8.zip && \  
yes |cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar ${JAVA_HOME}/jre/lib/security/  
# Define default command.  
CMD ["bash"]

