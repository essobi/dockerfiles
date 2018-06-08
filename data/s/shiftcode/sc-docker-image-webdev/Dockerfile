FROM node:7.9.0  
RUN apt-get update && \  
apt-get upgrade -y  
  
# Global install yarn package manager  
RUN apt-get install -y curl apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
  
# show yarn version  
RUN yarn --version  
  
# install angular-cli  
RUN yarn global add @angular/cli  
RUN ng --version  
  
# install aws cli  
RUN python --version  
  
RUN apt-get install -y \  
python-dev \  
python-pip  
  
# get the newest version of pip  
RUN pip install --upgrade pip  
RUN pip install --upgrade awscli  
  
# install the cloudfoundry cli  
RUN python --version  
RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary" | tar
-zx -C /usr/local/bin  
RUN cf --version  
  
ENTRYPOINT ["/bin/bash"]

