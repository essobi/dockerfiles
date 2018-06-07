FROM ubuntu:14.04  
ENV HOME /root  
ENV LAUNCH jenkins-slave.sh  
ENV SLAVE_NAME slave  
ENV SECRET_KEY
0be34b447c268f1db37fff13a0c51e09f7f6991b83d550342578766d284c0fb4  
ENV MASTER jenkins  
  
RUN echo "Asia/Taipei" > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata && \  
apt-get update && \  
apt-get install --no-install-recommends --no-install-suggests -y openjdk-7-jdk
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
echo '#!/bin/bash' > $HOME/$LAUNCH && \  
echo 'java -jar slave.jar -jnlpUrl
http://$MASTER:8080/computer/$SLAVE_NAME/slave-agent.jnlp -secret $SECRET_KEY'
>> $HOME/$LAUNCH && \  
chmod 755 $HOME/$LAUNCH  
  
WORKDIR /root  
  
COPY slave.jar slave.jar  
  
CMD ["/root/jenkins-slave.sh"]  

