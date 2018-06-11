FROM bradrydzewski/base  
  
ENV JAVA_OPTS -Xms128m -Xmx256m  
  
WORKDIR /home/ubuntu  
USER ubuntu  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN sudo add-apt-repository --yes ppa:webupd8team/java && \  
sudo apt-get -qq update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
sudo /usr/bin/debconf-set-selections && \  
sudo apt-get -y install oracle-java8-installer && \  
sudo apt-get -y install oracle-java8-set-default  
  
# Let's start with some basic stuff.  
RUN sudo apt-get update -qq && sudo apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ubuntu/ | sudo sh  
  
# Install the magic wrapper.  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN sudo chmod +x /usr/local/bin/wrapdocker  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
CMD ["wrapdocker"]  

