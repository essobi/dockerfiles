FROM sameersbn/gitlab-ci-multi-runner:latest  
MAINTAINER David Andlinger <david.andlinger@instant-it.at>  
  
ENV ANDROID_HOME=/opt/android-sdk  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-
common \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java8-installer \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk8-installer  
  
RUN wget -O /tmp/android-sdk-tools.zip
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip \  
&& unzip /tmp/android-sdk-tools.zip -d /opt/android-sdk/ \  
&& mkdir /opt/android-sdk/licenses \  
&& echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > /opt/android-
sdk/licenses/android-sdk-license \  
&& /opt/android-sdk/tools/bin/sdkmanager --update  
  
RUN /opt/android-sdk/tools/bin/sdkmanager "platform-tools" \  
&& /opt/android-sdk/tools/bin/sdkmanager "build-tools;19.1.0" "build-
tools;20.0.0" "build-tools;21.1.2" "build-tools;22.0.1" "build-tools;23.0.3"
"build-tools;24.0.3" "build-tools;25.0.2" \  
&& /opt/android-sdk/tools/bin/sdkmanager "platforms;android-7"
"platforms;android-8" "platforms;android-9" "platforms;android-10"
"platforms;android-11" "platforms;android-12" "platforms;android-13"
"platforms;android-14" "platforms;android-15" "platforms;android-16"
"platforms;android-17" "platforms;android-18" "platforms;android-19"
"platforms;android-20" "platforms;android-21" "platforms;android-22"
"platforms;android-23" "platforms;android-24" "platforms;android-25"
"platforms;android-26" \  
&& /opt/android-sdk/tools/bin/sdkmanager "extras;google;google_play_services"
"extras;google;m2repository" "extras;android;m2repository"
"extras;google;play_billing"  

