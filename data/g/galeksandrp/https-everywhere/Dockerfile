FROM electronicfrontierfoundation/https-everywhere-docker-base  
MAINTAINER William Budington "bill@eff.org"  
WORKDIR /opt  
ADD test/rules/requirements.txt test/rules/requirements.txt  
ADD test/chromium/requirements.txt test/chromium/requirements.txt  
RUN pip install -r test/rules/requirements.txt  
RUN pip install -r test/chromium/requirements.txt  
  
ENV FIREFOX /firefox-latest/firefox/firefox  
  
WORKDIR /opt  
  
RUN apt-get update && apt-get install -y wget npm nodejs-legacy python3-pip
sudo libffi-dev locales  
RUN wget
https://raw.githubusercontent.com/aboul3la/Sublist3r/master/requirements.txt  
RUN pip install -r requirements.txt  
RUN wget https://raw.githubusercontent.com/Foorack/httpse-ruleset-
generator/master/requirements.txt -O requirements3-foorack3.txt  
RUN pip3 install -r requirements3-foorack3.txt  
ADD requirements3.txt .  
RUN pip3 install -r requirements3.txt  
RUN mkdir -p ~/bin  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O
~/bin/jq  
RUN chmod +x ~/bin/jq  
RUN npm install -g galeksandrp/check-mixed-
content#245e56ad5fd5412bdad986276911e5460d9e48c6  
RUN locale-gen en_US.UTF-8  

