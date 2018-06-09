FROM ubuntu:16.04  
RUN apt-get update  
  
RUN apt-get install -y curl  
  
# install rvm Ruby stable  
RUN curl -sSL https://get.rvm.io | grep -v __rvm_print_headline | bash -s
stable --ruby  
  
RUN echo '[[ -s "/usr/local/rvm/bin/rvm" ]] && source "/usr/local/rvm/bin/rvm"
> /dev/null' >> ~/.bashrc  
  
# install rubyGem  
RUN /bin/bash -l -c 'rvm rubygems latest'  
  
# install bundle  
RUN /bin/bash -l -c 'gem install bundle'  
  
# install ruby 2.3.3  
RUN /bin/bash -l -c 'rvm install 2.3.3'  
RUN /bin/bash -l -c 'rvm --default use 2.3.3'  
  
# pre-install gem  
ADD Gemfile /  
RUN /bin/bash -l -c 'gem install bundler'  
RUN /bin/bash -l -c 'bundle install'  
  
# Android fo carabash  
RUN apt-get install wget unzip -y  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
(echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections) && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
ENV JAVA_OPTS="-Dsun.jnu.encoding=UTF-8 -Dfile.encoding=UTF-8"  
RUN cd /opt && \  
mkdir android_sdk && \  
cd android_sdk && \  
wget --output-document=tools.zip --quiet
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \  
unzip tools.zip && \  
rm -f tools.zip && \  
chown -R root.root tools && \  
echo y | yes | ./tools/bin/sdkmanager "platforms;android-25" "platform-tools"
"build-tools;25.0.3"  
  
ENV ANDROID_HOME=/opt/android_sdk  

