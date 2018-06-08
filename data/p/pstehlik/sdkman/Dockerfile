FROM pstehlik/ubuntu-java:java8  
MAINTAINER Philip Stehlik "p@pstehlik.com"  
# Install required tools.  
RUN \  
apt-get update && \  
apt-get install -y unzip curl --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
# install sdkman  
RUN curl -s "https://get.sdkman.io" | bash  
  
RUN sed -i 's/sdkman_auto_answer=false/sdkman_auto_answer=true/g'
/root/.sdkman/etc/config

