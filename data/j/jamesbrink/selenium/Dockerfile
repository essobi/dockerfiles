# Selenium  
#  
# VERSION 3.8.1  
FROM phusion/baseimage:0.9.22  
MAINTAINER James Brink, brink.james@gmail.com  
  
# Install needed system packages  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& useradd -g users -s /bin/bash -d /home/selenium -m selenium \  
&& apt-get install wget unzip openjdk-8-jdk-headless tightvncserver
libgconf-2.4 -y \  
&& apt-get install automake cmake clang gettext libx11-dev git build-essential
autopoint -y \  
&& cd /tmp \  
&& git clone https://github.com/joewing/jwm.git \  
&& cd jwm \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /tmp/jwm \  
&& apt-get remove automake cmake clang gettext libx11-dev git build-essential
autopoint -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN apt-get update  
RUN apt-get install -y chromium-browser  
RUN apt-get install -y firefox  
  
USER selenium  
WORKDIR /home/selenium/  
  
RUN mkdir /home/selenium/.vnc \  
&& echo "password" | vncpasswd -f > /home/selenium/.vnc/passwd \  
&& chmod 600 /home/selenium/.vnc/passwd  
  
RUN wget https://goo.gl/hvDPsK -O selenium_server.jar  
RUN mkdir -p /home/selenium/webdrivers \  
&& cd /home/selenium/webdrivers/ \  
&& wget
"https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz"
\  
&& wget
"https://chromedriver.storage.googleapis.com/2.34/chromedriver_linux64.zip" \  
&& tar xfvz geckodriver-v0.19.1-linux64.tar.gz \  
&& rm geckodriver-v0.19.1-linux64.tar.gz \  
&& unzip chromedriver_linux64.zip \  
&& rm chromedriver_linux64.zip \  
&& cd /home/selenium  
  
USER selenium  
ENV DISPLAY=:1  
# Add our docker-assets.  
ADD docker-assets/entrypoint.sh /home/selenium/entrypoint.sh  
ADD docker-assets/jwmrc /home/selenium/.jwmrc  
ADD docker-assets/xsession /home/selenium/.xsession  
  
# Expose vnc port.  
EXPOSE 5901  
CMD ["/home/selenium/entrypoint.sh"]  

