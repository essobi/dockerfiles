FROM ubuntu  
MAINTAINER Kirsten Hunter (synedra@gmail.com)  
RUN apt-get update  
RUN apt-get install -y ruby ruby-dev wget vim git curl ruby python3.4
python3-pip python-pip  
RUN pip install awsebcli  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sh -  
RUN apt-get install nodejs  
RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh  
RUN echo "deb https://packages.microsoft.com/repos/azure-cli/ wheezy main" |
tee /etc/apt/sources.list.d/azure-cli.list  
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys
52E16F86FEE04B979B07E28DB02C46DF417A0893  
RUN apt-get install apt-transport-https  
RUN apt-get update && apt-get install azure-cli  
ADD . /opt  
WORKDIR /opt  
RUN npm install  
RUN gem install travis  
ENTRYPOINT ["/bin/bash"]  

