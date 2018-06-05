FROM openjdk:8-jdk-slim-stretch  
# Declare some variables.  
# This is useful to have defaults, and helps programs that scam the Dockerfile  
# for metadata  
ENV BAMBOO_SERVER ""  
ENV AGENT_NAME "Bamboo docker agent"  
ENV AGENT_DESCRIPTION ""  
ENV BAMBOO_IGNORE_CERT false  
ENV BAMBOO_TOKEN ""  
# Update and install utilities and dependencies (as root)  
RUN apt update && apt install procps curl -y && apt clean  
  
# Create the bamboo user inside the container, to avoid running as root, set
the user as the default user,  
# and set the current directory to the user home.  
RUN groupadd -r bamboo && useradd --create-home -r -g bamboo bamboo  
USER bamboo:bamboo  
WORKDIR /home/bamboo  
  
# Add the script to run the agent  
COPY scripts/run-agent.sh run-agent.sh  
# Copy is ready script (useful in k8s)  
COPY scripts/is-ready is-ready  
# Gets agent version as a build parameter  
ARG version  
RUN curl --fail --silent -# https://packages.atlassian.com/maven-closedsource-
local/com/atlassian/bamboo/bamboo-agent/${version}/bamboo-agent-${version}.jar
--output "bamboo-agent.jar"  
  
# The entry point is set to run the bamboo agent  
ENTRYPOINT ["/bin/sh","run-agent.sh"]

