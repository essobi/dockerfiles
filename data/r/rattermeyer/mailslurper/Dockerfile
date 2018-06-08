FROM debian:jessie  
  
ENV MAILSLURPER_VERSION 1.12.1  
RUN useradd mailslurper && \  
mkdir -p /opt/mailslurper  
  
ADD
https://github.com/mailslurper/mailslurper/releases/download/${MAILSLURPER_VERSION}/mailslurper-${MAILSLURPER_VERSION}-linux.zip
/opt/mailslurper/mailslurper.zip  
  
WORKDIR /opt/mailslurper  
  
RUN apt-get update && apt-get install -y unzip && unzip
/opt/mailslurper/mailslurper.zip && \  
chown -R mailslurper:mailslurper /opt/mailslurper && \  
sed -i -e 's/localhost/0.0.0.0/g' config.json && \  
rm /opt/mailslurper/mailslurper.zip && \  
rm -rf /var/lib/apt/lists/*  
  
USER mailslurper  
  
ENTRYPOINT ["/opt/mailslurper/mailslurper"]  

