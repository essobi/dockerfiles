FROM neoalienson/nodejs:latest  
MAINTAINER neo [at] orz [dot] hk  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
CORDOVA_VERSION=6.0.0 \  
IONIC_VERSION=1.7.14  
# Install basics  
RUN npm install -g cordova@"$CORDOVA_VERSION" ionic@"$IONIC_VERSION" && \  
npm cache clear && \  
gem install sass  
  
# Webpack  
RUN npm install webpack webpack-dev-server -g  
  
# Create sample project  
RUN wget https://github.com/reactionic/reactionic-
kitchensink/archive/master.zip && \  
unzip master.zip && rm master.zip && \  
mv reactionic-kitchensink-master app && \  
cd app && npm install && webpack  
  
VOLUME /app  
  
WORKDIR /app  
EXPOSE 8080  
CMD ["webpack-dev-server", "--content-base", "build", "--host", "0.0.0.0"]  

