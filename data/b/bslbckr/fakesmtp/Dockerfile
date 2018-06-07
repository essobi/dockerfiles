FROM alpine:3.5  
RUN apk --update add openjdk8-jre && \  
rm -rf /var/cache/apk/* && \  
wget http://nilhcem.github.com/FakeSMTP/downloads/fakeSMTP-latest.zip -O
/tmp/fakeSMTP.zip && \  
mkdir -p /opt/fakeSMTP && \  
unzip /tmp/fakeSMTP.zip -d /opt/fakeSMTP && \  
rm /tmp/fakeSMTP.zip && \  
mkdir -p /opt/mails  
  
EXPOSE 25  
ENTRYPOINT ["java"]  
CMD ["-jar", "/opt/fakeSMTP/fakeSMTP-2.0.jar", "-s", "-b", "-o", "/opt/mails"]

