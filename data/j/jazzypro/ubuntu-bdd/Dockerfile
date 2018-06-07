FROM jazzypro/ubuntu-frontend:latest  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Install JDK  
#  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
  
#  
# Instal headless components  
#  
RUN apt-get install -y xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic x11-apps  
  
#  
# Add xvfb run script  
#  
COPY xvfb /etc/init.d/xvfb  
RUN chmod a+x /etc/init.d/xvfb  
  
#  
# Install ProtractorJS  
#  
RUN npm install -g protractor  
  
#  
# Install bless  
#  
RUN npm install -g bless  
  
#  
# Install bundler  
RUN gem install bundler --no-ri --no-rdoc  
  
#  
# Install Selenium dependencies  
#  
RUN webdriver-manager update  
  
#  
# Install Nginx  
#  
RUN apt-get install -y nginx  
  
#  
# Clear web_root so we don't have to do it at each build  
#  
RUN rm /usr/share/nginx/html/*  
  
#  
# Start Nginx  
#  
RUN service nginx start  
  

