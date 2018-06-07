FROM openjdk:8-jdk  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-
init_1.0.2_amd64 /usr/bin/dumb-init  
RUN chmod +x /usr/bin/dumb-init  
  
ENV ANDROID_COMPILE_SDK "25"  
ENV ANDROID_BUILD_TOOLS "25.0.2"  
ENV ANDROID_SDK_TOOLS "25.2.5"  
RUN apt-get update --yes \  
&& apt-get install --yes \  
wget \  
unzip \  
lib32stdc++6 \  
lib32z1 \  
nano \  
lsb-release \  
apt-transport-https \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "deb https://packages.gitlab.com/runner/gitlab-ci-multi-
runner/debian/ `lsb_release -cs` main" >
/etc/apt/sources.list.d/runner_gitlab-ci-multi-runner.list && \  
wget -q -O - https://packages.gitlab.com/gpg.key | apt-key add - && \  
apt-get update -y && \  
apt-get install -y gitlab-ci-multi-runner && \  
apt-get clean && \  
mkdir -p /etc/gitlab-runner/certs && \  
chmod -R 750 /etc/gitlab-runner && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget --quiet
https://dl.google.com/android/repository/tools_r${ANDROID_SDK_TOOLS}-linux.zip  
RUN unzip tools_r${ANDROID_SDK_TOOLS}-linux.zip -d /android-sdk-linux  
RUN chmod -R 777 /android-sdk-linux  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter android-${ANDROID_COMPILE_SDK}  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter platform-tools  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
-t 34  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter build-tools-${ANDROID_BUILD_TOOLS}  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter build-tools-24.0.3  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-android-m2repository  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-google-google_play_services  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-google-m2repository  
RUN export ANDROID_HOME=/android-sdk-linux  
RUN export PATH=$PATH:/android-sdk-linux/platform-tools/  
RUN echo y | /android-sdk-linux/tools/android --silent update sdk --no-ui
--all -t 68  
RUN echo y | /android-sdk-linux/tools/android create avd -n test -t android-24
--abi google_apis/armeabi-v7a  
  
ADD entrypoint /  
RUN chmod +x /entrypoint  
  
VOLUME ["/etc/gitlab-runner", "/home/gitlab-runner"]  
ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]  
  
RUN usermod -aG sudo gitlab-runner  
  
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]  

