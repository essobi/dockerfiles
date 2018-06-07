FROM circleci/python:3.6.1  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - &&
\  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y build-essential yarn nodejs imagemagick  
  
RUN sudo npm install -g serverless  
  
RUN sudo sed -i -e 's/# en_CA.UTF-8 UTF-8/en_CA.UTF-8 UTF-8/' /etc/locale.gen
&& \  
sudo sed -i -e 's/# fr_CA.UTF-8 UTF-8/fr_CA.UTF-8 UTF-8/' /etc/locale.gen && \  
sudo dpkg-reconfigure --frontend=noninteractive locales  
  
RUN sudo pip install awscli  

