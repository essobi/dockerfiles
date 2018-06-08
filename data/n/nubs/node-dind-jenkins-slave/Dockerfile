FROM tehranian/dind-jenkins-slave  
  
RUN apt-get update -qq && apt-get install -qqy nodejs npm jq  
  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 100  

