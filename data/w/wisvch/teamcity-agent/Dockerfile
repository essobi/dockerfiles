FROM jetbrains/teamcity-agent  
  
RUN curl -so /usr/local/share/ca-certificates/wisvch.crt
https://ch.tudelft.nl/certs/wisvch.crt && \  
chmod 644 /usr/local/share/ca-certificates/wisvch.crt && \  
update-ca-certificates  
RUN ln -sf /etc/ssl/certs/java/cacerts /usr/lib/jvm/oracle-
jdk/jre/lib/security/cacerts  
RUN curl -so /usr/lib/jvm/oracle-jdk/jre/lib/security/US_export_policy.jar \  
https://commissies.ch.tudelft.nl/~mark/UnlimitedJCEPolicyJDK8/US_export_policy.jar
&& \  
curl -so /usr/lib/jvm/oracle-jdk/jre/lib/security/local_policy.jar \  
https://commissies.ch.tudelft.nl/~mark/UnlimitedJCEPolicyJDK8/local_policy.jar  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN export DEBIAN_FRONTEND="noninteractive" && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y --no-install-recommends nodejs yarn jq && \  
rm -rf /var/lib/apt/lists/*  

