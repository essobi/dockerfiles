FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y curl unzip zip wget  
RUN /bin/bash -c "curl -s 'https://get.sdkman.io' | bash; \  
source /root/.sdkman/bin/sdkman-init.sh; \  
sed -i -e 's/sdkman_auto_answer=false/sdkman_auto_answer=true/g'
~/.sdkman/etc/config; \  
sdk install java 7u141-zulu; \  
sdk install java 8u131-zulu; \  
sdk install grails 2.3.6; \  
sdk install grails 3.2.9"

