FROM ubuntu:14.04  
MAINTAINER Talisto <https://github.com/talisto>  
  
ENV MCROUTER_DIR /usr/local/mcrouter  
ENV MCROUTER_REPO https://github.com/facebook/mcrouter.git  
ENV MCROUTER_RELEASE 36-0  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y git software-properties-common python-software-properties
sudo  
  
RUN mkdir -p $MCROUTER_DIR/repo && \  
cd $MCROUTER_DIR/repo && \  
git clone \--branch release-$MCROUTER_RELEASE $MCROUTER_REPO  
  
RUN cd $MCROUTER_DIR/repo/mcrouter/mcrouter/scripts && \  
./install_ubuntu_14.04.sh $MCROUTER_DIR && \  
./clean_ubuntu_14.04.sh $MCROUTER_DIR && rm -rf $MCROUTER_DIR/repo && \  
ln -s $MCROUTER_DIR/install/bin/mcrouter /usr/local/bin/mcrouter  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/spool/mcrouter  
  
ENV DEBIAN_FRONTEND newt  
  
ENTRYPOINT [ "mcrouter" ]  
CMD [ "--help" ]  

