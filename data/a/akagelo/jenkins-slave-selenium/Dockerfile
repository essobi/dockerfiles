# Version: 0.0.1  
FROM akagelo/jenkins-slave-xvnc  
MAINTAINER Oleg Vyukov <gelo@vyukov.ru>  
  
  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/chrome.list  
  
# обновляшки  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && apt-key update && apt-get update && apt-get install -y google-
chrome-stable iceweasel  
  
RUN wget -O /tmp/chromedriver.zip
http://chromedriver.storage.googleapis.com/2.21/chromedriver_linux64.zip &&
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && rm
/tmp/chromedriver.zip && chmod 755 /usr/local/bin/chromedriver  
  
RUN mkdir /opt/selenium && wget -O /opt/selenium/selenium.jar http://selenium-
release.storage.googleapis.com/2.52/selenium-server-standalone-2.52.0.jar  
  
#запуск сервисов через через самопальную систему иннициализации  
ADD etc/ /etc/  
  
ADD google-chrome /usr/bin/google-chrome  
  
RUN chmod +x /usr/bin/google-chrome  
  
#vnc порт  
EXPOSE 4444

