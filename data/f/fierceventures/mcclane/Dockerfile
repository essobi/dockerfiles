FROM clojure  
  
RUN apt-get update  
RUN apt-get install wget  
RUN apt-get install sudo  
  
# Install Maven  
run sudo apt-get install maven -y  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo bash -  
RUN sudo apt-get install nodejs  
RUN node -v  
RUN npm -v  
  
# Install Phantomjs  
RUN sudo apt-get install build-essential chrpath libssl-dev libxft-dev -y  
RUN sudo apt-get install libfreetype6 libfreetype6-dev -y  
RUN sudo apt-get install libfontconfig1 libfontconfig1-dev -y  
RUN wget
https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN sudo tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN sudo mv phantomjs-2.1.1-linux-x86_64 /usr/local/share  
RUN sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin  
RUN phantomjs --version  
  
# Install Terraform  
RUN wget
https://releases.hashicorp.com/terraform/0.11.6/terraform_0.11.6_linux_amd64.zip  
RUN unzip terraform_0.11.6_linux_amd64.zip  
RUN sudo mv terraform /usr/local/bin/  
RUN terraform --version  
  
# Install AWS CLI & EB CLI  
RUN sudo apt-get -y install python python-pip  
RUN sudo pip install awscli  
RUN pip install awsebcli  
RUN aws --version  
  
# Install Ruby and Bundler  
RUN apt-get install -y ruby ruby-dev  
RUN gem install bundler  

