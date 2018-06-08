# Java-8  
FROM java:openjdk-8-jdk  
MAINTAINER Tobias Wiens <https://github.com/tobwiens/proactive-scheduler-
dockerfile/>  
  
# Update and install tools  
RUN ["/bin/bash", "-c", "apt-get update && apt-get install git -y"]  
  
# Environment variables - determine the proactive version  
ENV PROACTIVE_HOME /data/scheduling  
  
# Create directories  
RUN ["/bin/bash", "-c", "mkdir /data && \  
mkdir /data/tmp"]  
  
# Get current master of ProActive repositiories  
WORKDIR /data  
  
# Build Scheduling  
RUN ["/bin/bash", "-c", " git clone
https://github.com/ow2-proactive/scheduling.git"]  
WORKDIR /data/scheduling  
RUN ["/bin/bash", "-c", "./gradlew dist"]  
  
# Create directories for the web interfaces  
RUN ["/bin/bash", "-c", "mkdir dist/war/studio && \  
mkdir dist/war/rm && \  
mkdir dist/war/scheduler"]  
  
# Get Studio interface  
WORKDIR /data/tmp/studio  
RUN ["/bin/bash", "-c", "git clone https://github.com/ow2-proactive/studio.git
&& \  
mv studio/app/* /data/scheduling/dist/war/studio/ && \  
rm -rf /data/tmp/studio"]  
  
# Get Scheduler and Resource Manager Interface  
WORKDIR /data/tmp  
RUN ["/bin/bash", "-c", "git clone
https://github.com/ow2-proactive/scheduling-portal.git && \  
cd scheduling-portal && \  
./gradlew war && \  
mv scheduler-portal/build/libs/scheduler-portal-*.war
/data/scheduling/dist/war/scheduler.war && \  
mv rm-portal/build/libs/rm-portal-*.war /data/scheduling/dist/war/rm.war && \  
rm -rf /data/tmp/scheduling-portal"]  
  
EXPOSE 8080  
# Run proactive scheduler with zero nodes  
ENTRYPOINT ["/data/scheduling/bin/proactive-server", "-ln" ,"0",
"-Dproactive.useIPaddress=true"]  

