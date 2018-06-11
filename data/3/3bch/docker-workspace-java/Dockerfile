FROM 3bch/docker-workspace-base:ubuntu-LTS  
MAINTAINER 3bch  
  
# Install SDKMAN  
RUN curl -s "https://get.sdkman.io" | bash  
  
# Install Gradle & Groovy  
RUN set -x && \  
echo "sdkman_auto_answer=true" > /root/.sdkman/etc/config && \  
bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install java && sdk
install gradle && sdk install groovy && sdk install vertx"  

