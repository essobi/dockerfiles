FROM openjdk:8-jre-alpine  
MAINTAINER Raúl Cruz  
  
# Create user java:java  
RUN addgroup -S java && adduser -S -G java java  
WORKDIR /home/java  
  
# Install extensions and entrypoint script  
# Install Java Cryptography Extension  
RUN mkdir -p /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security && \  
wget --no-check-certificate --header "Cookie: oraclelicense=accept-
securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip" && \  
unzip -p jce_policy-8.zip UnlimitedJCEPolicyJDK8/local_policy.jar >
/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/local_policy.jar && \  
unzip -p jce_policy-8.zip UnlimitedJCEPolicyJDK8/US_export_policy.jar >
/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/US_export_policy.jar && \  
rm jce_policy-8.zip && \  
# Entrypoint script  
# Using RUN instead of "COPY --chown=java:java entrypoint.sh ." because of
--chown incompatibility with docker version prior to 17.09)  
wget
https://raw.githubusercontent.com/abaenglish/openjdk/master/8-jre/entrypoint.sh
&& \  
chmod u+x entrypoint.sh && \  
# Set permissions to non-root user  
chown java:java *  
  
# Run as user java:java  
USER java:java  

