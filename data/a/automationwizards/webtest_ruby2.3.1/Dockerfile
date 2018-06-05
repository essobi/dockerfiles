FROM automationwizards/ruby2.3.1:trusty  
MAINTAINER Justin Commu  
  
# Set timezone  
RUN echo "US/Eastern" > /etc/timezone && \  
dpkg-reconfigure \--frontend noninteractive tzdata  
  
# Add Chrome Repo  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
  
# Update the repositories & install packages  
RUN apt-get update -y && apt-get install -y \  
firefox \  
google-chrome-stable \  
libav-tools \  
unzip \  
fonts-ipafont-gothic \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable \  
xvfb && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Chrome WebDriver  
RUN CHROMEDRIVER_VERSION='2.27' && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
  
# Disable the SUID sandbox so that Chrome can launch without being in a
privileged container.  
# One unfortunate side effect is that `google-chrome --help` will no longer
work.  
RUN dpkg-divert --add --rename --divert /opt/google/chrome/google-chrome.real
/opt/google/chrome/google-chrome && \  
echo "#!/bin/bash\nexec /opt/google/chrome/google-chrome.real --disable-
setuid-sandbox \"\$@\"" > /opt/google/chrome/google-chrome && \  
chmod 755 /opt/google/chrome/google-chrome  

