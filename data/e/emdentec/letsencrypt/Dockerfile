FROM debian:jessie  
MAINTAINER emdentec ltd. <docker@emdentec.com>  
  
RUN apt-get update && \  
apt-get install -y \  
git  
  
ENV WORK_DIR /usr/lib/letsencrypt  
ENV VERSION 0.5.0  
RUN mkdir $WORK_DIR && \  
cd $WORK_DIR && \  
git init && \  
git remote add origin https://github.com/letsencrypt/letsencrypt && \  
git fetch -q origin && \  
git reset -q --hard v${VERSION}  
  
RUN $WORK_DIR/letsencrypt-auto -q --help && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
ln -s $WORK_DIR/letsencrypt-auto /bin/letsencrypt  
  
RUN mkdir -p /var/www/letsencrypt  
  
VOLUME /etc/letsencrypt  
VOLUME /var/www/letsencrypt  
  
WORKDIR $WORK_DIR  
  
ENTRYPOINT ["letsencrypt", "--no-self-upgrade"]

