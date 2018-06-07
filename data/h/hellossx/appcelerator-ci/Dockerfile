FROM ubuntu  
MAINTAINER Scott Wilcox <scott@dor.ky>  
  
RUN apt-get -y update  
RUN apt-get -y install curl git software-properties-common gcc-multilib
lib32z1 lib32stdc++6  
  
# Install node6  
RUN cd /tmp && curl -sL https://deb.nodesource.com/setup_6.x -o
/tmp/nodesource_setup.sh && chmod +x /tmp/nodesource_setup.sh &&
/tmp/nodesource_setup.sh  
RUN apt-get update -y && apt-get install nodejs -y  
RUN npm install -g appcelerator titanium jasmine alloy tisdk  
  
# install java, only oracles will do  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
RUN export JAVA_HOME=/usr/lib/jvm/java-8-oracle/  
  
# install android sdk  
RUN mkdir -p /usr/local/android  
RUN cd /usr/local/android && \  
wget http://dl.google.com/android/android-sdk_r24.2-linux.tgz && \  
tar -xvf android-sdk_r24.2-linux.tgz && \  
export ANDROID_HOME=/usr/local/android/android-sdk-linux && \  
export PATH=$PATH:$ANDROID_HOME/tools && \  
export PATH=$PATH:$ANDROID_HOME/platform-tools && \  
cd $ANDROID_HOME && \  
(while sleep 3; do echo "y"; done) | $ANDROID_HOME/tools/android update sdk -u
--filter 1,2,3,5  
  
# add a non root user  
RUN useradd -c "Testing user" testing -s /bin/bash -m  
  
# Now install the SDK we're working with  
# This can't be done here as we're going to need a username/password for  
# Appcelerator's SDK install and build commands.  
RUN runuser -l testing -c 'tisdk install 6.0.3.GA'  
RUN chown -R testing /usr/local/android  
  
CMD ["/bin/bash"]  

