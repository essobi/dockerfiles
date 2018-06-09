FROM stilesb/stack:latest  
USER root  
RUN apt-get install -y libglib2.0-dev libcairo2-dev libcogl-pango-dev gtk2.0 \  
libwebkit-dev libtinfo-dev dh-autoreconf libncurses5-dev python-software-
properties  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash  
RUN apt-get install -y nodejs  
RUN npm -g install closurecompiler  
RUN mkdir -p /opt/web/api/.stack-work /opt/web/client/.stack-work \  
/opt/web/server/.stack-work /home/robot/.stack /home/robot/.local/bin && \  
chown robot -R /opt/web /home/robot  
USER robot  
ENV PATH /home/robot/.local/bin:$PATH  
WORKDIR /opt/web/api  
ADD api/stack.yaml api/api.cabal ./  
RUN stack setup  
RUN stack install --dependencies-only  
WORKDIR /opt/web/server  
ADD server/stack.yaml server/server.cabal ./  
RUN stack setup  
RUN stack install --dependencies-only  
WORKDIR /opt/web/client  
ADD client/config/stack-base.yaml stack.yaml  
ADD client/config/stack-ghcjs-base.yaml stack-ghcjs.yaml  
ADD client/config/client-base.cabal client.cabal  
RUN stack --stack-yaml=stack-ghcjs.yaml setup  
RUN stack setup  
RUN stack install --dependencies-only  
ENV PATH $PATH:/home/robot/.stack/programs/x86_64-linux  
RUN ln -s /home/robot/.stack/programs/x86_64-linux/ghc-8.0.1/bin/ghc
/home/robot/.local/bin/ghc  
RUN stack install hsc2hs happy  
RUN stack --stack-yaml=stack-ghcjs.yaml install --dependencies-only  
WORKDIR /opt/web  
CMD ["tail", "-f", "/dev/null"]  

