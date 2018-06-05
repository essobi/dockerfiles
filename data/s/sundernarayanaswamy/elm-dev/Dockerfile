FROM microsoft/dotnet  
  
MAINTAINER sunder.narayanaswamy@gmail.com  
  
RUN bash -c "curl -sL https://deb.nodesource.com/setup_6.x | bash -"  
  
RUN apt-get update && apt-get install -y nodejs inotify-tools emacs git tree
silversearcher-ag  
  
RUN yarn global add firebase-tools bs-platform \  
elm elm-test elm-format elm-oracle \  
tern js-beautify jshint  
  
RUN apt-get -y autoremove && \  
apt-get -y clean && \  
apt-get -y autoclean && \  
rm -rf /var/lib/apt/lists/*  
  
# http server to be tied to port 80  
EXPOSE 8080  
# websocket ports for brunch watch  
EXPOSE 9485-9495  
# websocket port for livereload  
EXPOSE 35729  
WORKDIR /root  
  
CMD /bin/bash  
  
# tail -f /dev/null  

