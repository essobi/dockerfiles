FROM circleci/android:api-26-alpha  
  
# Define our node version to run  
ENV NODE_VERSION 6.7.0  
# Define our gradle version to install  
ENV GRADLE_VERSION 3.3  
# To download node binaries into our home directory  
WORKDIR /home/circleci  
  
# Install gradle  
RUN wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
bin.zip \  
&& sudo unzip -d /opt gradle-$GRADLE_VERSION-bin.zip \  
&& sudo ln -s /opt/gradle-$GRADLE_VERSION/bin/gradle /usr/local/bin  
  
# Install node  
RUN wget https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz \  
&& tar xzvf node-v$NODE_VERSION-linux-x64.tar.gz \  
&& sudo chown -Rv root.root node-v6.7.0-linux-x64 \  
&& sudo cp -Rvi node-v6.7.0-linux-x64/bin /usr/local \  
&& sudo cp -Rvi node-v6.7.0-linux-x64/include /usr/local \  
&& sudo cp -Rvi node-v6.7.0-linux-x64/lib /usr/local \  
&& sudo cp -Rvi node-v6.7.0-linux-x64/share /usr/local  
  
# Install AWS commandline tools  
RUN pip install awscli --upgrade --user \  
&& sudo ln -s ~/.local/bin/aws /usr/bin  

