FROM ubuntu:14.04  
ENV MCROUTER_DIR /usr/local/mcrouter  
ENV MCROUTER_REPO https://github.com/facebook/mcrouter.git  
ENV MCROUTER_TAG v0.9.0  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y git && \  
mkdir -p $MCROUTER_DIR/repo && \  
cd $MCROUTER_DIR/repo && git clone \--branch $MCROUTER_TAG $MCROUTER_REPO && \  
cd $MCROUTER_DIR/repo/mcrouter/mcrouter/scripts && \  
./install_ubuntu_14.04.sh $MCROUTER_DIR && \  
./clean_ubuntu_14.04.sh $MCROUTER_DIR && rm -rf $MCROUTER_DIR/repo && \  
ln -s $MCROUTER_DIR/install/bin/mcrouter /usr/local/bin/mcrouter  
  
ENV DEBIAN_FRONTEND newt  
  
RUN mkdir /var/spool/mcrouter  
VOLUME /var/spool/mcrouter  
  
RUN mkdir /etc/mcrouter  
VOLUME /etc/mcrouter  
  
EXPOSE 11211  
ENTRYPOINT ["mcrouter"]  
CMD ["--port=11211", "--validate-config=run", "--config-
file=/etc/mcrouter/mcrouter.conf"]  

