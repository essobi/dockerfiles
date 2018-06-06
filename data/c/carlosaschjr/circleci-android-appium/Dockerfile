FROM circleci/android:api-27-node8-alpha  
  
RUN mkdir -p ~/.npm-global && \  
mkdir -p /home/circleci/workspace && \  
mkdir -p /home/circleci/code  
  
RUN sudo apt-get install libqt5widgets5 && \  
sudo pip install Appium-Python-Client && \  
sdkmanager "system-images;android-27;google_apis;x86" && \  
npm config set prefix '~/.npm-global' && \  
echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc && \  
npm install -g appium  
  
RUN sh -c 'echo "no" | avdmanager create avd -f -n test -k "system-
images;android-27;google_apis;x86"'  
  
COPY wait-for-device.sh /wait-for-device.sh  
  
ENV PATH="$HOME/.npm-global/bin:$PATH"  
WORKDIR /home/circleci/code  

