FROM ubuntu  
  
MAINTAINER Harm Pauw <h.pauw@prowareness.nl>  
  
RUN apt-get update && \  
apt-get install -y wget  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
  
RUN apt-get update && \  
apt-get install -y \  
google-chrome-stable \  
xvfb \  
default-jre \  
fluxbox \  
fonts-liberation \  
zip  
  
COPY startnode.sh /  
  
# Download latest version of selenium server  
RUN SELENIUM_URL=http://selenium-release.storage.googleapis.com/`wget -qO -
http://selenium-release.storage.googleapis.com/ | \  
awk -vRS="</Key>" '{gsub(/.*<Key>/,"");print}' | \  
grep standalone | \  
sort -rn | \  
head -n 1` && \  
wget -qO selenium-server-standalone.jar $SELENIUM_URL  
  
# Download latest version of chrome driver  
RUN CPUBIT=`getconf LONG_BIT` && \  
CHROMEDRIVER_URL=http://chromedriver.storage.googleapis.com/2.`wget -qO -
http://chromedriver.storage.googleapis.com/ | \  
awk -vRS="</Key>" '{gsub(/.*<Key>/,"");print}' | \  
grep linux$CPUBIT | \  
sed 's/^[0-9].//' | sort -rn | head -n 1` && \  
wget -qO chromedriver.zip $CHROMEDRIVER_URL  
  
RUN unzip chromedriver.zip  
  
RUN useradd -m -U selenium  
RUN chmod 755 /startnode.sh && chmod 755 /chromedriver && chmod 644 /selenium-
server-standalone.jar  
  
RUN ln -s /lib/x86_64-linux-gnu/libudev.so.1.3.5 /usr/lib/libudev.so.0  
  
USER selenium  
ENV SCREEN_DIMENSION 1920x1080x24  
ENV MAX_INSTANCES 5  
ENV HOME /home/selenium  
  
EXPOSE 4444  
CMD ["/startnode.sh"]  

