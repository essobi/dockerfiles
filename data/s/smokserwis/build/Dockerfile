FROM smokserwis/build:jdk8  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
clean-apt-install nodejs  
  
RUN wget https://downloads.gradle.org/distributions/gradle-4.8-bin.zip && \  
mkdir /opt/gradle && \  
unzip -d /opt/gradle gradle-4.8-bin.zip && \  
update-alternatives --install /usr/bin/gradle gradle
/opt/gradle/gradle-4.8/bin/gradle 100  
  
RUN npm install -g --unsafe-perm bower gulp karma  
  
RUN mkdir -p /usr/adk && \  
cd /usr/adk && \  
wget http://files.itachi.pl/sdk-tools-linux-3859397.zip && \  
unzip sdk-tools-linux-3859397.zip && \  
rm sdk-tools-linux-3859397.zip  
  
ENV ANDROID_HOME=/usr/adk  
  
RUN mkdir /usr/adk/licenses && \  
echo -e
"\n8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb78af6dfcb131a6481e"
> /usr/adk/licenses/android-sdk-license && \  
echo -e "\n504667f4c0de7af1a06de9f4b1727b84351f2910" >
/usr/adk/licenses/android-sdk-preview-license && \  
echo y | /usr/adk/tools/bin/sdkmanager "build-tools;28.0.0-rc2"
"platforms;android-27" "platform-tools" "tools" "extras;android;m2repository"
"extras;google;m2repository" "extras;google;google_play_services"  
  
LABEL NodeJS 8  

