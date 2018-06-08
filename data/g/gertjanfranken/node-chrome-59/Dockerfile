# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
# NOTE: DO *NOT* EDIT THIS FILE. IT IS GENERATED.  
# PLEASE UPDATE Dockerfile.txt INSTEAD OF THIS FILE  
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
FROM selenium/node-base:3.11.0-californium  
LABEL authors=SeleniumHQ  
  
USER root  
  
#============================================  
# Google Chrome  
#============================================  
  
RUN apt-get update -qqy  
  
RUN wget --no-verbose -O /tmp/chrome_59.deb
https://www.slimjet.com/chrome/download-
chrome.php?file=lnx%2Fchrome64_59.0.3071.86.deb \  
&& dpkg -i /tmp/chrome_59.deb || true  
  
RUN sudo apt-get -y install -f  
  
RUN rm /tmp/chrome_59.deb  
  
#=================================  
# Chrome Launch Script Wrapper  
#=================================  
  
COPY wrap_chrome_binary /opt/bin/wrap_chrome_binary  
RUN chmod a+x /opt/bin/wrap_chrome_binary  
RUN /opt/bin/wrap_chrome_binary  
  
USER seluser  
  
#============================================  
# Chrome webdriver  
#============================================  
  
ARG CHROME_DRIVER_VERSION="2.32"  
RUN CD_VERSION=$(if [ ${CHROME_DRIVER_VERSION:-latest} = "latest" ]; then echo
$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE); else
echo $CHROME_DRIVER_VERSION; fi) \  
&& echo "Using chromedriver version: "$CD_VERSION \  
&& wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CD_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/selenium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CD_VERSION \  
&& chmod 755 /opt/selenium/chromedriver-$CD_VERSION \  
&& sudo ln -fs /opt/selenium/chromedriver-$CD_VERSION /usr/bin/chromedriver  
  
COPY generate_config /opt/bin/generate_config  
  
# Generating a default config during build time  
RUN sudo chmod 777 /opt/bin/generate_config  
RUN /opt/bin/generate_config > /opt/selenium/config.json  

