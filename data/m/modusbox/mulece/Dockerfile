FROM java  
MAINTAINER info@modusbox.com  
ARG version=3.8.0  
ARG ports=8081  
RUN if [ "$version" != "3.8.0" ] && [ "$version" != "3.7.0" ] && [ "$version"
!= "3.6.1" ] && [ "$version" != "3.6.0" ] && [ "$version" != "3.5.0" ]; then
echo "----- Unsopported version: $version \-----" && return 1; fi  
  
RUN if [ "$version" = "3.8.0" ]; then cd ~ && wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/${version}/mule-standalone-${version}.tar.gz && echo
"d9279b3f0373587715613341a16483f3 mule-standalone-${version}.tar.gz" | md5sum
-c ; fi  
RUN if [ "$version" = "3.7.0" ]; then cd ~ && wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/${version}/mule-standalone-${version}.tar.gz && echo
"6814d3dffb5d8f308101ebb3f4e3224a mule-standalone-${version}.tar.gz" | md5sum
-c ; fi  
RUN if [ "$version" = "3.6.1" ]; then cd ~ && wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/${version}/mule-standalone-${version}.tar.gz && echo
"3a018c579ae2cd172569c8f8cf3a44b8 mule-standalone-${version}.tar.gz" | md5sum
-c ; fi  
RUN if [ "$version" = "3.6.0" ]; then cd ~ && wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/${version}/mule-standalone-${version}.tar.gz && echo
"e475eca6f954280f08e6a3f52893360c mule-standalone-${version}.tar.gz" | md5sum
-c ; fi  
RUN if [ "$version" = "3.5.0" ]; then cd ~ && wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/${version}/mule-standalone-${version}.tar.gz && echo
"4a94356f7401ac8be30a992a414ca9b9 mule-standalone-${version}.tar.gz" | md5sum
-c ; fi  
  
RUN cd /opt && tar xvzf ~/mule-standalone-${version}.tar.gz && rm ~/mule-
standalone-${version}.tar.gz && ln -s /opt/mule-standalone-${version}
/opt/mule  
  
ENV MULE_HOME /opt/mule  
  
VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps",
"/opt/mule/domains"]  
  
WORKDIR /opt/mule  
  
CMD [ "/opt/mule/bin/mule" ]  
  
EXPOSE $ports

