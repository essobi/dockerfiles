FROM xblaster/generic_node  
#FROM nodexb  
#FROM pitchoun  
ADD src /pitch  
WORKDIR /pitch  
#RUN npm install bufferutil --save  
#RUN npm install utf-8-validate --save  
#RUN npm install v8-profiler --save  
#RUN npm install phantomjs --save  
#RUN npm install parse-ms --save  
#RUN npm install grunt --save  
#RUN npm install express --save  
#RUN npm install mailgun-js --save  
#RUN npm install plur --save  
#RUN npm install node-inspector --save  
#RUN npm install mongoose --save  
#RUN npm install babel-core --save  
#RUN npm install plur@1 --save  
#RUN npm install  
RUN npm install  
RUN bower install --allow-root  
  
EXPOSE 8080  
CMD grunt serve:dist --force  

