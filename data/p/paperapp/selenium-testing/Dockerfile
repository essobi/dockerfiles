FROM node:6.6.0  
MAINTAINER "Shane Fast" <shane@get-paper.com>  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv EA312927 \  
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list \  
&& apt-get update \  
&& apt-get install -y -qq curl \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections \  
&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true"
| debconf-set-selections \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886
\  
&& apt-get update \  
&& apt-get -y install oracle-java8-installer \  
&& apt-get clean  
RUN curl -o /usr/local/bin/jq http://stedolan.github.io/jq/download/linux64/jq
\  
&& chmod +x /usr/local/bin/jq  
  
RUN apt-get -y install wget \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& sh -c 'echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list' \  
&& apt-get -y install apt-transport-https \  
&& apt-get update \  
&& apt-get -y install google-chrome-stable  
  
RUN npm install webdriver-manager protractor gulp chromedriver -g  
# Define working directory.  
WORKDIR /data  
CMD ["-"]  
ENTRYPOINT ["jq"]  

