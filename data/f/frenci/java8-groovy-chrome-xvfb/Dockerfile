FROM java:8  
MAINTAINER Francois Misslin <francois@revinate.com>  
  
#=========  
# Env variables  
#=========  
ENV GROOVY_VERSION 2.3.9  
#=========  
# Install groovy from GVM  
#=========  
# Installs curl and GVM  
RUN apt-get update && apt-get install -y \  
curl \  
unzip  
  
RUN curl -s get.gvmtool.net | bash  
  
# Installs Groovy from GVM  
RUN /bin/bash -c "source /root/.gvm/bin/gvm-init.sh && gvm install groovy
${GROOVY_VERSION}"  
ENV GROOVY_HOME /root/.gvm/groovy/current  
ENV PATH $GROOVY_HOME/bin:$PATH  
  
  
#=========  
# Adding Headless Selenium with Chrome and Firefox  
#=========  
# Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
RUN apt-get update && apt-get install -y \  
google-chrome-stable  
  
# Chrome driver  
RUN wget -O /tmp/chromedriver.zip
http://chromedriver.storage.googleapis.com/2.16/chromedriver_linux64.zip  
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/  
RUN chmod ugo+rx /usr/bin/chromedriver  
  
# Dependencies to make "headless" selenium work  
RUN apt-get -y install \  
gtk2-engines-pixbuf \  
libxtst6 \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-base \  
xfonts-cyrillic \  
xfonts-scalable \  
xvfb  
  
# Starting xfvb as a service  
ENV DISPLAY=:99  
ADD xvfb /etc/init.d/  
RUN chmod 755 /etc/init.d/xvfb  
  

