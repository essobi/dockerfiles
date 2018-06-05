FROM node:8  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
RUN chmod +x /usr/local/bin/tini  
  
RUN git clone https://github.com/kuropen/mastodon-alliance-bot /bot  
  
WORKDIR /bot  
  
RUN git checkout feature/encode  
  
VOLUME /bot/config  
  
RUN yarn install  
  
ADD run.sh /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
CMD ["/usr/local/bin/run"]  
  

