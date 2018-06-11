FROM tomzo/gocd-ide:1.0.0  
RUN echo "ide ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/ide && \  
chmod 0440 /etc/sudoers.d/ide  
  
RUN apt-get update && apt-get install -y terminator  
  
RUN apt-get update && apt-get install -y wget && \  
echo 'Downloading IntelliJ IDEA' && \  
wget https://download.jetbrains.com/idea/ideaIC-2018.1.2.tar.gz -O
/tmp/intellij.tar.gz -q && \  
echo 'Installing IntelliJ IDEA' && \  
mkdir -p /opt/intellij && \  
tar -xf /tmp/intellij.tar.gz --strip-components=1 -C /opt/intellij && \  
rm /tmp/intellij.tar.gz  
  
ADD start_terminal.sh /usr/local/bin/terminal  
ADD run_intellij.sh /usr/local/bin/intellij  
ADD run.sh /sbin/run.sh  
  
RUN chmod +x /usr/local/bin/terminal && \  
chmod +x /usr/local/bin/intellij && \  
chmod +x /sbin/run.sh  
  
CMD ["/sbin/run.sh"]  

