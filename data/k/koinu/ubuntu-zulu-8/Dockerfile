FROM ubuntu:latest  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
0xB1998361219BD9C9 \  
&& echo 'deb http://repos.azulsystems.com/ubuntu stable main' >
/etc/apt/sources.list.d/zulu.list \  
&& apt-get -qq update \  
&& apt-get -qqy install zulu-8 wget unzip \  
&& wget -qO /tmp/ZuluJCEPolicies.zip \  
http://www.azulsystems.com/sites/default/files/images/ZuluJCEPolicies.zip \  
&& cd /tmp \  
&& echo "8021a28b8cac41b44f1421fd210a0a0822fcaf88d62d2e70a35b2ff628a8675a
ZuluJCEPolicies.zip" | \  
sha256sum \--check \--strict \--quiet \  
&& cd /usr/lib/jvm/zulu-8-amd64/jre/lib/security \  
&& unzip -qjo /tmp/ZuluJCEPolicies.zip \  
ZuluJCEPolicies/local_policy.jar \  
ZuluJCEPolicies/US_export_policy.jar \  
&& chmod g-w local_policy.jar US_export_policy.jar \  
&& sed -i \  
-e 's_^securerandom\.source=.*_securerandom.source=/dev/urandom_' \  
-e 's_^securerandom\.strongAlgorithms=.*_securerandom.strongAlgorithms=NativePRNGNonBlocking:SUN_' \  
/usr/lib/jvm/zulu-8-amd64/jre/lib/security/java.security \  
&& apt-get -qq \--auto-remove purge wget unzip \  
&& apt-get -qq clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG=C.UTF-8  

