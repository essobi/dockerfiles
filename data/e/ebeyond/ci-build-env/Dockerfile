FROM ubuntu:16.04  
MAINTAINER Marc Ende <me@e-beyond.de>  
ENV REFRESHED_AT 2018-01-26  
RUN apt-get update -qq  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update -qq  
RUN apt-get purge -y docker docker.io  
RUN apt-get install -y build-essential  
RUN apt-get install -y nodejs  
RUN apt-get install -y rsync  
RUN apt-get install -y apt-transport-https  
RUN apt-get install -y ca-certificates  
RUN apt-get install -y software-properties-common  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update -qq  
RUN apt-get install -y docker-ce  
RUN apt-get autoremove  
RUN curl -sL -o /bin/gimme https://raw.githubusercontent.com/travis-
ci/gimme/master/gimme  
RUN chmod +x /bin/gimme  
RUN curl -sL -o /usr/local/bin/increment_version.sh
https://raw.githubusercontent.com/fmahnke/shell-
semver/master/increment_version.sh  
RUN chmod +x /usr/local/bin/increment_version.sh  
RUN rm -rf /var/lib/apt/lists/*  
RUN npm install -g bower  
RUN npm install -g typescript  
  
WORKDIR /app  
ONBUILD ADD . /app  
  
CMD ["bash"]  

