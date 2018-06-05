FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y apt-utils  
RUN apt-get install -y openjdk-8-jre && apt-get -y install curl  
RUN apt-get install -y php7.0-cli  
RUN apt-get install -y wget  
RUN apt-get install -y php7.0-xml  
RUN apt-get install -y php-mbstring  
RUN apt-get install -y php7.0-intl  
RUN apt-get install -y xvfb  
RUN apt-get install -y firefox xvfb python-pip  
RUN apt-get install -y xmlstarlet  
RUN apt-get install -y nano  
RUN apt-get install -y git  
RUN apt-get install -y ssh  
  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
  
RUN mkdir test  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN curl -o atlassian-bamboo-6.0.3.tar.gz -SL
https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-6.0.3.tar.gz && tar xvzf atlassian-bamboo-6.0.3.tar.gz && rm atlassian-
bamboo-6.0.3.tar.gz  
  
RUN mv /atlassian-bamboo-6.0.3 /home/bamboo  
  
RUN chmod -R 700 /home/bamboo  
  
RUN mkdir /home/bamboo-home  
  
#START - copio le key per SSH  
####RUN chmod -R 700 /home/bamboo-home  
####RUN git clone https://bitbucket.org/nextshop_rende/bamboo.git
/home/bamboo-home/authorized_keys_ssh  
####RUN cd /home/bamboo-home/authorized_keys_ssh  
####RUN chmod 0600 dockercloud  
####CMD find . ! -name dockercloud ! -name dockercloud.pub -maxdepth 1 -type f
-delete  
#END - copio le key per SSH  
RUN chmod -R 700 /home/bamboo  
  
RUN { \  
echo 'bamboo.home=/home/bamboo-home'; \  
} > /home/bamboo/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties  
  
#START configurazione invio mail con GMAIL  
RUN mv /home/bamboo/atlassian-bamboo/WEB-INF/lib/javax.mail-1.5.2.jar
/home/bamboo/lib/  
RUN mv /home/bamboo/atlassian-bamboo/WEB-INF/lib/javax.mail-api-1.5.6.jar
/home/bamboo/lib/  
  
RUN xmlstarlet ed -P -S -L -s /Server/Service/Engine/Host/Context -t elem -n
ResourceTMP -v "" \  
-i //ResourceTMP -t attr -n "name" -v "mail/GmailSmtpServer" \  
-i //ResourceTMP -t attr -n "auth" -v "Container" \  
-i //ResourceTMP -t attr -n "type" -v "javax.mail.Session" \  
-i //ResourceTMP -t attr -n "mail.smtp.host" -v "smtp.gmail.com" \  
-i //ResourceTMP -t attr -n "mail.smtp.port" -v "465" \  
-i //ResourceTMP -t attr -n "mail.smtp.auth" -v "true" \  
-i //ResourceTMP -t attr -n "mail.smtp.user" -v "nextshop.rende.ci@gmail.com" \  
-i //ResourceTMP -t attr -n "password" -v "nextshop" \  
-i //ResourceTMP -t attr -n "mail.smtp.starttls.enable" -v "true" \  
-i //ResourceTMP -t attr -n "mail.smtp.socketFactory.class" -v "javax.net.ssl.SSLSocketFactory" \  
-r //ResourceTMP -v Resource \  
/home/bamboo/conf/server.xml  
#END  
RUN curl -fsSLO
https://get.docker.com/builds/Linux/x86_64/docker-17.03.1-ce.tgz  
RUN tar --strip-components=1 -xvzf docker-17.03.1-ce.tgz -C /usr/bin  
  
#aggiunta per allineare la versione di Docker sul server Docker Cloud  
#EXPORT DOCKER_API_VERSION=1.23  
ENV DOCKER_API_VERSION="1.23"  
EXPOSE 8085  
EXPOSE 54663  
EXPOSE 5432  
CMD /home/bamboo/bin/start-bamboo.sh -fg  
  

