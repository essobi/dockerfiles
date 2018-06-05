FROM ruby:2.5-alpine  
MAINTAINER apiology  
  
#  
# Had to remove the QT5 packages for Alpine. To reproduce issue:  
  
# docker run -v /tmp:`pwd`/tmp -it alpine:3.4 sh  
  
# apk update && apk add qt5-qtwebkit-dev ruby ca-certificates ruby-dev gcc
make libc-dev g++ xvfb dbus mesa-dri-swrast && QMAKE=/usr/lib/qt5/bin/qmake
gem install --no-document capybara-webkit headless  
  
# ruby <<EOF  
# require 'capybara'  
# require 'capybara-webkit'  
# require 'headless'  
# Capybara::Webkit.configure do |config|  
# config.debug = true  
# config.allow_unknown_urls  
# end  
# Headless.new.start  
# s = Capybara::Session.new(:webkit)  
# s.visit('http://google.com')  
# s.save_screenshot('tmp/test.png')  
# s.click_link('Sign in')  
# EOF  
  
  
# # To resolve issue, we use qt4:  
  
# docker run -v /tmp:`pwd`/tmp -it alpine:3.4 sh  
  
# apk update && apk add tzdata libxml2 libxml2-dev libxslt libxslt-dev qt-dev
imagemagick imagemagick-dev gcc g++ make ruby-dev ruby xvfb && gem install
--no-document capybara-webkit headless  
  
  
  
# ruby <<EOF  
# require 'capybara'  
# require 'capybara-webkit'  
# require 'headless'  
# Capybara::Webkit.configure do |config|  
# config.debug = true  
# config.allow_unknown_urls  
# end  
# Headless.new.start  
# s = Capybara::Session.new(:webkit)  
# s.visit('http://google.com')  
# s.save_screenshot('tmp/test.png')  
# s.click_link('Sign in')  
# EOF  
  
  
  
#  
# https://github.com/thoughtbot/capybara-webkit/issues/885  
# https://github.com/thoughtbot/capybara-webkit/wiki/Installing-Qt-and-
compiling-capybara-webkit  
# https://github.com/thoughtbot/capybara-webkit/issues/983  
#  
  
  
#  
# prereqs for scraping, bundles, fetching and debugging  
#  
RUN apk update && \  
apk add \  
netcat-openbsd \  
py-pip \  
nodejs \  
xvfb \  
git \  
icu-dev \  
cmake \  
qt-dev  
  
ENV DISPLAY "localhost:0"  
  
#  
# I forget why this exists.  
#  
ADD cacert.pem /root/bin/cacert.pem  

