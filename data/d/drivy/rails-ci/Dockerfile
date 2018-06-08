FROM circleci/ruby:2.3.3-node-browsers  
RUN sudo apt-get update  
RUN sudo apt-get install mysql-client  
  
# Install Phraseapp  
RUN mkdir -p ~/bin/  
RUN wget https://github.com/phrase/phraseapp-
client/releases/download/1.4.5/phraseapp_linux_amd64 -O ~/bin/phraseapp  
RUN chmod +x ~/bin/phraseapp  
ENV PATH "$PATH:~/bin"  
# Install Phantomjs  
ENV PHANTOM_JS phantomjs-2.1.1-linux-x86_64  
RUN sudo apt-get install build-essential chrpath libssl-dev libxft-dev
libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev  
RUN sudo wget
https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 -O
/usr/local/share/$PHANTOM_JS.tar.bz2  
RUN sudo tar xvjf /usr/local/share/$PHANTOM_JS.tar.bz2 -C /usr/local/share/  
RUN sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin  
  
# Install Heroku Toolbelt  
RUN sudo apt-get install software-properties-common apt-transport-https ca-
certificates  
RUN sudo add-apt-repository "deb https://cli-
assets.heroku.com/branches/stable/apt ./"  
RUN curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -  
RUN sudo apt-get update  
RUN sudo apt-get install heroku  

