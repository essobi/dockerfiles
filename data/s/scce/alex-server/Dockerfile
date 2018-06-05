FROM openjdk:8  
# Set our working driectory for the rest of this file  
WORKDIR /usr/src/alex  
  
# Install Chrome, with all the needed deepencies,  
# including the Chrome Driver and the Marionette / Gecko Driver for Selenium.  
# This also includes the Xvfb to run them both in a headless mode.  
RUN apt update && apt install -y --no-install-recommends \  
chromium \  
iceweasel \  
xvfb \  
unzip \  
libgconf-2-4 \  
&& rm -rf /var/lib/apt/lists/*e  
# install the latest version of firefox  
# according to https://linuxconfig.org/how-to-install-latest-firefox-browser-
on-debian-9-stretch-linux  
RUN wget -O FirefoxSetup.tar.bz2
"https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" \  
&& mkdir /opt/firefox \  
&& tar xjf FirefoxSetup.tar.bz2 -C /opt/firefox/ \  
&& mv /usr/lib/firefox-esr/firefox-esr /usr/lib/firefox-esr/firefox-esr_orig \  
&& ln -s /opt/firefox/firefox/firefox /usr/lib/firefox-esr/firefox-esr \  
&& rm FirefoxSetup.tar.bz2  
  
# install ALEX  
# use the tu depot for the latest build until v1.4.0 is released on github  
RUN wget -O alex.war "https://depot.tu-dortmund.de/9rcgz"  
# get latest chrome driver  
RUN wget
https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip -d ./ \  
&& rm chromedriver_linux64.zip \  
&& chmod +x chromedriver  
  
# get latest firefox driver  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
\  
&& tar -xf geckodriver-v0.19.1-linux64.tar.gz \  
&& rm geckodriver-v0.19.1-linux64.tar.gz \  
&& chmod +x geckodriver  
  
# Last refinements to the envoirment and the image.  
ENV DISPLAY :99  
# run a virtual display with full hd resolution  
RUN Xvfb :99 -screen 0 1920x1080x16 &  
  
# per default, ALEX runs on port 8000  
EXPOSE 8000  
# execute ALEX  
ENTRYPOINT java -jar alex.war "--chromeDriver=/usr/src/alex/chromedriver" "--
geckoDriver=/usr/src/alex/geckodriver"  

