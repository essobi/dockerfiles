FROM drush/drush:8-alpine  
  
LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"  
  
USER root  
  
# SSH config.  
RUN mkdir -p /root/.ssh  
ADD config/ssh /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
  
# Install Bash.  
RUN apk add --update --no-cache bash procps && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Java.  
RUN apk add --update --no-cache openjdk7-jre-base && \  
rm -rf /var/lib/apt/lists/*  
  
# Install druflow & assemble gradle & groovy.  
ENV JAVA_HOME=/usr  
RUN git clone https://github.com/aroq/druflow.git \  
&& cd druflow \  
&& ./gradlew assemble  

