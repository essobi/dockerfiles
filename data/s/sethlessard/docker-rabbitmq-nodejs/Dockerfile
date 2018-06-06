FROM ubuntu:14.04  
# Update the system  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
build-essential \  
wget \  
curl  
  
# Add the rabbitmq.com APT repository to /etc/apt/sources.list.d  
RUN echo 'deb http://www.rabbitmq.com/debian/ testing main' | tee
/etc/apt/sources.list.d/rabbitmq.list  
# Add public key to trusted key list  
RUN wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-
key add -  
  
# Install rabbitmq  
RUN apt-get update && apt-get install -y rabbitmq-server  
  
RUN rabbitmq-plugins enable rabbitmq_management rabbitmq_management_agent  
  
RUN mkdir /data  
RUN mkdir /data/rabbit  
  
# Define mount points.  
VOLUME ["/data/rabbit/log", "/data/rabbit/mnesia"]  
  
# Define environment variables.  
ENV RABBITMQ_HOME /data/rabbit  
ENV RABBITMQ_LOG_BASE $RABBITMQ_HOME/log  
ENV RABBITMQ_MNESIA_BASE $RABBITMQ_HOME/mnesia  
  
# Install NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install nodejs -y  
  
RUN node --version  
RUN npm --version  
  
EXPOSE 5672  
EXPOSE 15672  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

