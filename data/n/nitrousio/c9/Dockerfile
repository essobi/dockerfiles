FROM nitrousio/nodejs:latest  
MAINTAINER Nitrous.IO <hello@nitrous.io>  
  
RUN \  
su action -l -c /bin/bash -c \  
'git clone https://github.com/cj1990s/cloud9.git /home/action/c9'  
  
RUN \  
su action -l -c /bin/bash -c \  
'cd /home/action/c9 && \  
npm install'  
  
RUN mkdir /volumes  
  
VOLUME ["/volumes"]  
  
EXPOSE 3131  
ENV NITROUS_SSH_ENABLED false  
ENV NITROUS_APP_PORT 3131  
ENV IDE_USERNAME user  
ENV IDE_PASSWORD <__random__>  
  
ADD files/run.sh /home/action/c9/run.sh  
  
CMD ["/bin/bash", "-l", "/home/action/c9/run.sh"]  

