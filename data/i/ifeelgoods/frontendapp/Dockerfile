# build it:  
# sudo docker build -t backoffice .  
# start it:  
FROM ubuntu:14.04  
  
RUN apt-get update && apt-get upgrade -y && apt-get install nodejs phantomjs
npm python-software-properties software-properties-common git imagemagick xdg-
utils firefox wget xvfb ssh-askpass -y && apt-get clean  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN add-apt-repository ppa:brightbox/ruby-ng && apt-get update && apt-get
install ruby2.2 ruby2.2-dev -y && apt-get clean  
  
ENV DISPLAY :99  
  
RUN wget
ftp.mozilla.org/pub/mozilla.org/firefox/releases/34.0.5/linux-x86_64/en-
US/firefox-34.0.5.tar.bz2  
RUN tar -xjvf firefox-34.0.5.tar.bz2  
RUN rm -rf /opt/firefox*  
RUN mv firefox /opt/firefox34.0.5  
RUN ln -sf /opt/firefox34.0.5/firefox /usr/bin/firefox  
  
ENV FIREFOX_BIN /usr/bin/firefox  
  
RUN npm install -g grunt-cli bower  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENV HOME /home/user  
  
RUN useradd --create-home --home-dir $HOME user \  
&& chown -R user:user /usr/src/app  
  
ENV GEM_HOME $HOME/ruby/gems  
ENV GEM_PATH $GEM_HOME:/lib/ruby/gems/2.0  
ENV GEM_CACHE $GEM_HOME/cache  
ENV PATH $PATH:$HOME/ruby/gems/bin  
ENV PATH ./node_modules/.bin:$PATH  

