  
#
================================================================================================================  
#  
# A fake SMTP server to get mails sent by your app and put them in a directory  
#  
# @see Original docker project => https://github.com/munkyboy/docker-fakesmtp  
# @see FakeSMTP official source code => https://github.com/Nilhcem/FakeSMTP  
# @see FakeSMPT official site => http://nilhcem.github.io/FakeSMTP/  
#
================================================================================================================  
# Base image, java required  
FROM openjdk:8-jre-alpine  
  
# Environment configuration  
ENV FAKE_SMTP_MAIL_DIR="/var/mail" \  
FAKE_SMTP_APP_DIR="/opt/FakeSMTP"  
# Install fake smtp server  
RUN apk --no-cache add curl \  
&& mkdir -p -m 777 $FAKE_SMTP_MAIL_DIR \  
&& mkdir -p -m 777 $FAKE_SMTP_APP_DIR \  
&& cd $FAKE_SMTP_APP_DIR \  
&& curl -o fakeSMTP.zip -k -SL
http://nilhcem.github.com/FakeSMTP/downloads/fakeSMTP-latest.zip \  
&& unzip fakeSMTP.zip \  
&& rm -f fakeSMTP.zip \  
&& mv fakeSMTP-*.jar fakeSMTP.jar  
  
# To listen like a real stmp server  
EXPOSE 25  
# Where mails are stored by the server  
WORKDIR $FAKE_SMTP_MAIL_DIR  
VOLUME $FAKE_SMTP_MAIL_DIR  
  
# Command to run the server in the container  
CMD java -jar $FAKE_SMTP_APP_DIR/fakeSMTP.jar -s -b -o $FAKE_SMTP_MAIL_DIR  

