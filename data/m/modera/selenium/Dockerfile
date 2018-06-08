FROM blacklabelops/java:ubuntu.jdk8  
# it is important that we use ubuntu 14.04 which has XVFB v1.15, in newer
versions it does not open TCP ports  
# when --listen-tcp flag is used
(https://bugzilla.redhat.com/show_bug.cgi?id=1340432)  
  
# ca-certificates is needed for application be able to verify certificates
(such as wget)  
RUN apt-get update -qqy && \  
apt-get -qy --no-install-recommends install \  
bzip2 \  
ca-certificates \  
unzip \  
wget \  
vim \  
xvfb \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# =========  
# Selenium  
# =========  
RUN mkdir -p /opt/selenium \  
&& wget --no-verbose https://selenium-
release.storage.googleapis.com/3.0/selenium-server-standalone-3.0.1.jar -O
/opt/selenium/selenium-server-standalone.jar  
  
# ==============  
# Google Chrome  
# ==============  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qy \  
&& apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable} \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN mkdir -p /opt/selenium/drivers  
  
#==================  
# Chrome webdriver  
#==================  
ARG CHROME_DRIVER_VERSION=2.27  
RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium/drivers \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/drivers/chromedriver
/opt/selenium/drivers/chromedriver-$CHROME_DRIVER_VERSION \  
&& chmod 755 /opt/selenium/drivers/chromedriver-$CHROME_DRIVER_VERSION \  
&& ln -fs /opt/selenium/drivers/chromedriver-$CHROME_DRIVER_VERSION
/usr/bin/chromedriver  
  
# Adding --no-sandbox prevents Chrome from crashing (<defunc>) on a  
# "Attempting bi-dialect session, assuming Postel's Law holds true on the
remote end"  
# step when a new session is scheduled  
RUN sed -i -e 's/"$HERE\/chrome"/"$HERE\/chrome" --no-sandbox/g'
/opt/google/chrome/google-chrome  
  
# should help preventing Chrome from hanging occasionally  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
COPY entry-point.sh /opt/bin/  
RUN chmod +x /opt/bin/entry-point.sh  
  
ENTRYPOINT ["/opt/bin/entry-point.sh"]

