FROM leansoft/java8  
  
ENV AMC_VERSION 1.0.1  
ENV AMC_HOME /home/amc  
ENV AMC_BIN_NAME atlassian-marketplace-collector-$AMC_VERSION.jar  
  
RUN (crontab -l ; echo "37 3 * * * $JAVA_HOME/bin/java -jar
$AMC_HOME/$AMC_BIN_NAME >> /home/amc/logs/amc.log 2>&1") | crontab -  
  
RUN mkdir $AMC_HOME  
RUN mkdir $AMC_HOME/logs  
  
RUN curl -L -o $AMC_HOME/$AMC_BIN_NAME https://github.com/wyrzyk/atlassian-
marketplace-collector/releases/download/$AMC_VERSION/$AMC_BIN_NAME  
  
WORKDIR $AMC_HOME/logs  
CMD cron && tail -f /dev/null

