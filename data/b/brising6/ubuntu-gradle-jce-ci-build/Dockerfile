FROM java:8  
  
ENV PORT=8080 \  
GRADLE_HOME=/usr/bin/gradle-2.14 \  
PATH=$PATH:/usr/bin/gradle-2.14/bin:/meta/.cli  
  
EXPOSE 8080  
  
ADD . /meta  
  
WORKDIR /usr/bin  
  
RUN wget -q https://services.gradle.org/distributions/gradle-2.14-bin.zip -O
gradle.zip \  
&& unzip -q gradle.zip \  
&& rm gradle.zip \  
&& wget https://nodejs.org/dist/v4.2.1/node-v4.2.1-linux-x64.tar.gz \  
&& tar -xzf "node-v4.2.1-linux-x64.tar.gz" -C /usr/local --strip-components=1
\  
&& rm "node-v4.2.1-linux-x64.tar.gz" \  
&& node -v \  
&& npm -v \  
&& cd /meta \  
&& unzip -jo -d ${JAVA_HOME}/jre/lib/security ./unlimited_jce_policy.zip \  
&& gradle build \  
&& gradle test \  
&& npm install -g phantomjs \  
&& npm install -g webpack \  
&& npm install -g fbjs \  
&& npm install -g typescript \  
&& git config --global user.name CI-BuildBot \  
&& git config --global user.email svc_payments_ci \  
&& tar -xzf cf-cli*.tgz -C /usr/bin/  

