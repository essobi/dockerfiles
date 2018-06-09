FROM switchback/debian  
  
RUN apt-get update && \  
apt-get install -y git && \  
rm -rf /var/lib/apt/lists/*  
  
# create all the directories that we need  
RUN mkdir -p $HOME/.ssh  
RUN mkdir -p /var/default  
RUN mkdir -p /var/project  
RUN mkdir -p /var/workspace  
  
# defaults for client  
VOLUME /var/default  
# project directory  
VOLUME /var/project  
# workspace to do work  
VOLUME /var/workspace  
  
# git repository ssh url  
ENV REPO null  
# git branch name  
ENV BRANCH master  
  
# set working directory  
WORKDIR /var/workspace  
  
# add script to run  
ADD *.sh /usr/local/bin/  
  
CMD /bin/bash /usr/local/bin/setup.sh  

