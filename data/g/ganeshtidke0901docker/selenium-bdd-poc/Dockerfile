FROM ubuntu  
MAINTAINER Avijit Samanta  
  
# Update and install s/w  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk  
RUN apt-get install -y git maven  
RUN apt-get install -y xvfb libxi6 libgconf-2-4  
RUN apt-get install -y wget unzip curl gnupg  
  
# Install Chrome driver for Ubuntu  
RUN wget -N
http://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip  
RUN unzip chromedriver_linux64.zip -d /usr/local/share  
RUN rm chromedriver_linux64.zip  
RUN chmod +x /usr/local/share/chromedriver  
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver  
RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver  
  
# Install Chrome  
#RUN wget https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
-  
#RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
#RUN apt-get -yqq update  
#RUN apt-get -yqq install google-chrome-stable  
#RUN rm -rf /var/lib/apt/lists/*  
#RUN set -xe \  
# && apt-get update \  
# && apt-get install -y --no-install-recommends ca-certificates curl socat \  
# && apt-get install -y --no-install-recommends sudo \  
# && rm -rf /var/lib/apt/lists/*  
RUN set -xe \  
&& curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable \  
&& rm -rf /var/lib/apt/lists/*  
  
# Clone Git repo and build/execute automation package  
RUN git clone -b master --single-branch
https://github.com/ganeshtidke0901/selenium-bdd-poc.git  
WORKDIR /selenium-bdd-poc  
  

