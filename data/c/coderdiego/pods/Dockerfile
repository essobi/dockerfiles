FROM ruby:alpine  
  
# Ruby is required by CocoaPods and is more difficult to install than node so
we base our image off the Ruby official docker image  
# Create non-root user for CodoaPods  
RUN \  
apk update && \  
apk upgrade && \  
apk add git curl && \  
adduser -D -g GECOS app  
  
# We need curl for pod install  
# Preparation for running yarn install and pod install  
# COPY ios/Podfile ios/Podfile.lock ios/VianaBlue.xcodeproj /usr/src/app/  
# Cocoapods gem install (as special user)  
# Pod install  
  
USER app  
COPY docker-entrypoint.sh /home/app/  
ENV GEM_HOME=/home/app/.gem  
RUN gem install cocoapods  
  
# && \  
# GEM_HOME=$HOME/.gem $HOME/.gem/bin/pod install && \  
# echo "export GEM_HOME=\$HOME/.gem && export PATH=\$GEM_HOME/bin:\$PATH" >>
~/.bashrc  
# Ports and volumes  
VOLUME /usr/src/app  
  
# Working dir is the shared volume  
WORKDIR /usr/src/app/ios  
ENTRYPOINT ["/home/app/docker-entrypoint.sh"]  
CMD ["ash"]  

