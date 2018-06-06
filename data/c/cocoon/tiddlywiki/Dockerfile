FROM cocoon/python  
  
RUN apt-get update  
  
RUN apt-get install -y g++ make checkinstall wget  
RUN mkdir /opt/node  
WORKDIR /opt/node  
#RUN mkdir ~/node_js_src && cd $_  
RUN wget -N http://nodejs.org/dist/node-latest.tar.gz  
RUN tar xzvf node-latest.tar.gz && cd node-v* && ./configure && checkinstall
&& dpkg -i node_*  
  
# Install npm  
#RUN apt-get install -y software-properties-common && apt-get clean  
#RUN add-apt-repository -y ppa:chris-lea/node.js && apt-get update  
#RUN apt-get install -y nodejs && apt-get clean  
# Install tiddlywiki  
RUN npm install -g tiddlywiki  
  
# Setup wiki volume  
VOLUME /var/lib/tiddlywiki  
WORKDIR /var/lib/tiddlywiki  
  
EXPOSE 8080  
# Meta  
CMD tiddlywiki mywiki --init server && tiddlywiki mywiki --server 8080
$:/core/save/all text/plain text/html user "" 0.0.0.0  
  
# with wiki prefix  
#CMD tiddlywiki mywiki --init server && tiddlywiki mywiki --server 8080
$:/core/save/all text/plain text/html user "" 0.0.0.0 wiki

