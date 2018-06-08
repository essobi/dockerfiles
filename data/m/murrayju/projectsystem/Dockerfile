FROM python:2  
WORKDIR /usr/src/app  
  
ADD requirements.txt /usr/src/app/  
RUN pip install -r requirements.txt  
  
RUN apt-get update && apt-get install -y ca-certificates curl  
  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.31/SHASUMS256.txt.asc  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
RUN gpg --keyserver pgp.mit.edu --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D  
  
ENV NODE_VERSION 0.10.32  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
RUN npm install -g karma  
  
ADD package.json /usr/src/app/  
RUN npm install  
  
ADD bower.json /usr/src/app/  
RUN bower install --config.interactive=false \--allow-root  
  
ADD . /usr/src/app/  
RUN grunt prebuild  
RUN grunt build  
  
EXPOSE 5000  
CMD python ./manager.py $DB_1_PORT_27017_TCP_ADDR  

