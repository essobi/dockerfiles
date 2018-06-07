FROM debian:stable  
RUN apt-get update && apt-get install -y \  
wget \  
xz-utils\  
&& rm -rf /var/lib/apt/lists/*  
WORKDIR /tmp  
RUN wget -qO- "https://developer.salesforce.com/media/salesforce-cli/sfdx-
linux-amd64.tar.xz" | tar xJf -  
RUN bash ./sfdx/install  
RUN apt-get update && apt-get install -y \  
openssl \  
xxd \  
openjdk-8-jre-headless \  
xvfb \  
chromedriver \  
git\  
&& rm -rf /var/lib/apt/lists/*  
RUN wget -q https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& (dpkg -i google-chrome-stable_current_amd64.deb \  
|| (apt-get update && apt-get -fy install && rm -rf /var/lib/apt/lists/*)) \  
&& ln -s /opt/google/chrome/google-chrome /usr/bin/chrome \  
&& rm google-chrome-stable_current_amd64.deb  

