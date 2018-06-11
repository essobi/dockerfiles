FROM jetbrains/teamcity-server  
  
RUN curl -so /usr/local/share/ca-certificates/wisvch.crt
https://ch.tudelft.nl/certs/wisvch.crt && \  
chmod 644 /usr/local/share/ca-certificates/wisvch.crt && \  
update-ca-certificates  
RUN /usr/lib/jvm/oracle-jdk/jre/bin/keytool -noprompt -keystore
/usr/lib/jvm/oracle-jdk/jre/lib/security/cacerts \  
-storepass changeit -importcert -alias wisvch -file /usr/local/share/ca-certificates/wisvch.crt  
RUN curl -so /usr/lib/jvm/oracle-jdk/jre/lib/security/US_export_policy.jar \  
https://commissies.ch.tudelft.nl/~mark/UnlimitedJCEPolicyJDK8/US_export_policy.jar
&& \  
curl -so /usr/lib/jvm/oracle-jdk/jre/lib/security/local_policy.jar \  
https://commissies.ch.tudelft.nl/~mark/UnlimitedJCEPolicyJDK8/local_policy.jar  

