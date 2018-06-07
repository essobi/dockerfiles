FROM slogsdon/develop-base  
  
RUN \  
sudo apt-get install -y --no-install-recommends \  
default-jdk \  
&&\  
sudo rm -rf /var/lib/apt/lists/* &&\  
curl -O
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein &&\  
curl -O https://raw.githubusercontent.com/ninjudd/drip/master/bin/drip &&\  
sudo mv drip lein /usr/local/bin &&\  
sudo chmod a+x /usr/local/bin/drip /usr/local/bin/lein &&\  
lein &&\  
drip  
  
ENV LEIN_JAVA_CMD drip  

