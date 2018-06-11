from alpine  
  
MAINTAINER milanaleksic <milanaleksic@gmail.com>  
  
ENV PATH $PATH:/usr/lib/node_modules/bin  
  
ADD ocd-clean /util/  
  
RUN apk --update add nodejs curl tar && \  
npm install --prefix /usr/lib/node_modules/ -g typescript && \  
mkdir -p /usr/lib/node_modules/bin && \  
mv /usr/bin/node /usr/lib/node_modules/bin/node && \  
curl -L https://www.npmjs.com/install.sh | sh && \  
rm -rf /usr/bin/npm /home/developer/* && \  
ln -s /usr/lib/node_modules/npm/bin/npm-cli.js /usr/bin/npm && \  
npm install tsd -g && \  
npm install http-server -g && \  
apk del curl tar && \  
sh /util/ocd-clean / && \  
mkdir -p /home/developer/workspace  
  
WORKDIR /home/developer/workspace  

