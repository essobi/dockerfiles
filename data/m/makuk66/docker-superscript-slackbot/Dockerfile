FROM debian:latest  
  
MAINTAINER Martijn Koster "https://github.com/makuk66"  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y openssl ca-certificates curl git build-essential && \  
apt-get install -y vim  
  
RUN (curl -sL https://deb.nodesource.com/setup | bash -) && \  
apt-get install -y nodejs  
  
RUN groupadd ssjs && \  
useradd --system --shell /bin/bash --comment 'superscriptjs dedicated user'
\--uid 5000 --gid ssjs --home /home/ssjs ssjs && \  
mkdir /home/ssjs ssjs && chown ssjs:ssjs /home/ssjs  
  
COPY run-slackbot.sh /home/ssjs/  
COPY myserver.js /home/ssjs/  
RUN chown ssjs:ssjs /home/ssjs/run-slackbot.sh /home/ssjs/myserver.js  
RUN chmod u+x /home/ssjs/run-slackbot.sh  
USER ssjs  
RUN (cd /home/ssjs && git clone https://github.com/silentrob/superscript.git
&& chown -R ssjs:ssjs superscript)  
RUN (cd /home/ssjs/superscript && npm install)  
RUN (cd /home/ssjs && ./superscript/bin/bot-init.js slackbot --client slack &&
cd slackbot && npm install)  
RUN bash -c 'mv /home/ssjs/{run-slackbot.sh,myserver.js} /home/ssjs/slackbot/'  
RUN echo 'cd /home/ssjs/slackbot' > /home/ssjs/.bash_history  
RUN echo 'bash /home/ssjs/slackbot/run-slackbot.sh' >>
/home/ssjs/.bash_history  

