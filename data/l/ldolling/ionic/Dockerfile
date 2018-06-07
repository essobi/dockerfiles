FROM webratio/nodejs-with-android-sdk  
  
  
#################  
# System Tools  
#################  
RUN apt-get update  
RUN apt-get install -y git nano ruby-compass python python-dev python-
distribute python-pip  
RUN npm install -g cordova ionic grunt-cli bower  
RUN gem install sass  
  
#################  
# SSH key for github.com  
#################  
RUN mkdir /root/.ssh  
RUN touch /root/.ssh/known_hosts  
RUN apt-get install -y openssh-client  
RUN ssh-keyscan github.com > /root/.ssh/known_hosts  

