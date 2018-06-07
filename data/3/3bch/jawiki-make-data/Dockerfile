FROM openjdk:8-jdk  
MAINTAINER 3bch  
  
# Install SDKMAN  
RUN curl -s "https://get.sdkman.io" | bash  
  
# Install Groovy  
RUN set -x && \  
echo "sdkman_auto_answer=true" > /root/.sdkman/etc/config && \  
bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install groovy"  
# Install Jedis (Grape)  
RUN /bin/bash -c "source ~/.sdkman/bin/sdkman-init.sh && grape install
redis.clients jedis 2.8.1"  
# Copy Script Files  
COPY ./script /root/script  
  
# Copy Config File  
COPY ./config /root/config  
  
  
CMD ["/root/script/run-all.sh"]  
  

