FROM java:latest  
  
MAINTAINER Helpful version: 0.2  
ADD https://cli.run.pivotal.io/stable?release=linux64-binary&source=github
/tmp/cf-cli.tgz  
RUN mkdir -p /usr/local/bin \  
&& tar -z -x -v -f /tmp/cf-cli.tgz -C /usr/local/bin \  
&& rm -f /tmp/cf-cli.tgz  
  
RUN (curl -fL https://getcli.jfrog.io | sh) \  
&& mv jfrog /usr/local/bin/  
  
# webapp build/deploy stuff  
RUN wget https://deb.nodesource.com/setup_8.x \  
&& chmod +x setup_8.x \  
&& ./setup_8.x \  
&& apt-get install -y nodejs ruby-full build-essential zip \  
&& gem install sass  
  
# chrome+webdriver requirements  
RUN apt-get install -y fonts-liberation libappindicator1 libatk-bridge2.0-0
libgtk-3-0 xdg-utils \  
&& wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg -i google-chrome-stable_current_amd64.deb \  
&& rm -f google-chrome-stable_current_amd64.deb  
  
# jq (command-line json processor used by test scripts)  
RUN cd /opt \  
&& mkdir jq \  
&& wget -O ./jq/jq http://stedolan.github.io/jq/download/linux64/jq \  
&& chmod +x ./jq/jq \  
&& ln -s /opt/jq/jq /usr/local/bin  

