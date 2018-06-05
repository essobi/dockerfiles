FROM area51/jenkins-slave  
MAINTAINER Peter Mount <peter@retep.org>  
  
COPY docker-entrypoint.sh /  
COPY start-ssh /usr/local/bin/  
RUN chmod 555 /usr/local/bin/start-ssh /docker-entrypoint.sh &&\  
addgroup jenkins abuild &&\  
addgroup cloud abuild  
  
#ENTRYPOINT ["docker-entrypoint.sh"]  
ENTRYPOINT []  
  
# Our required packages. Java is from the parent image  
RUN wget -O /etc/apk/keys/jenkins-5782b282.rsa.pub
http://packages.area51.onl/alpine/jenkins-5782b282.rsa.pub &&\  
echo http://packages.area51.onl/alpine >>/etc/apk/repositories &&\  
apk add --update \  
alpine-sdk \  
autoconf \  
automake \  
cmake \  
cvs \  
git \  
mercurial \  
subversion \  
valgrind \  
vim  
  
# Don't remove apt lists as we want something present in most builds if we
then add additional packages  
# rm -rf /var/lib/apt/lists/*  

