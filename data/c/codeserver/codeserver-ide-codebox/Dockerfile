FROM codeserver/runtime-image-base:latest  
MAINTAINER Neil Ellis hello@neilellis.me  
  
RUN cd /usr/local/ && git clone https://github.com/neilellis/codebox.git && cd
codebox && npm install . && \  
cd /usr/local/codebox && /usr/local/codebox/node_modules/grunt-cli/bin/grunt  
  
ADD bin/ide.sh /etc/service/ide/run  
ADD etc/codebox.settings.json /usr/local/etc/codebox.settings.json  
RUN chmod 755 /etc/service/ide/run  
EXPOSE 8080  

