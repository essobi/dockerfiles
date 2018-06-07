#  
# kinetic-sim Dockerfile  
#  
# https://github.com/sbates130272/docker-kinetic-sim  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# Set the maintainer  
MAINTAINER Stephen Bates (sbates130272) <sbates@raithlin.com>  
  
# Install the Seagate/kinetic-java code from Github, we also need  
# java (jdk and jre) , git and Apache maven so we install that too. As  
# per Dockerfile best practices we split this up to get snapshots  
# along the way  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y openjdk-7-jre  
RUN apt-get install -y maven  
RUN git clone https://github.com/Seagate/kinetic-java.git kinetic-java  
  
# Now set JAVA_HOME using the ENV command and build the simulator  
# using maven. Note the cd and mvn must be on the same line to ensure  
# maven runs in the right folder.  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
RUN cd kinetic-java && mvn clean package -DskipTests  
  
# The simulator runs on port 8123 by default so we expose that  
# port.  
EXPOSE 8123  
# Define the default entry point to this container to be the kinetic  
# simulator start script. This forces this container to only be a  
# kinetic simulator.  
CMD [""]  
ENTRYPOINT ["/root/kinetic-java/bin/startSimulator.sh"]  

