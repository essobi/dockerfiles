FROM ruby:2.3.3  
ARG BUNDLE_GITHUB__COM  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y qt5-default libqt5webkit5-dev gstreamer1.0-plugins-base
gstreamer1.0-tools gstreamer1.0-x xvfb  
  
RUN gem update --system && \  
gem install bundler  

