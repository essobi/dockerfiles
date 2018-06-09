FROM debian:wheezy  
  
# install hugo  
ENV HUGO_VERSION 0.19  
ENV HUGO_BINARY hugo_${HUGO_VERSION}-64bit.deb  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
/tmp/hugo.deb  
RUN dpkg -i /tmp/hugo.deb \  
&& rm /tmp/hugo.deb  
  
# additionally install git, rsync for deployment  
RUN apt-get update && apt-get install -y \  
git \  
rsync  
  
# default deploy source path  
ENV DEPLOY_SRC /root/src  
# default deploy destination path  
ENV DEPLOY_DEST /root/dest  
# default deploy destination path  
ENV GIT_BRANCH master  
# placeholder for the git repository  
ENV GIT_URL ""  
ADD deploy.sh /usr/local/bin/deploy.sh  
ENTRYPOINT ["/bin/bash" ]  
CMD ["/usr/local/bin/deploy.sh"]  

