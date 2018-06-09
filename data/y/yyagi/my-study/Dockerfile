FROM ruby:2.4.1  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
npm cmake unzip libnss3  
RUN CHROMEDRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
RUN apt-get -y install google-chrome-stable  
RUN npm cache clean && npm install n -g && n stable && ln -sf
/usr/local/bin/node /usr/bin/node  
RUN apt-get purge -y nodejs npm  
RUN npm install -g yarn  
RUN mkdir /app  
WORKDIR /app  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle install  
COPY package.json /app/package.json  
COPY yarn.lock /app/yarn.lock  
RUN yarn  
ADD . /app  

