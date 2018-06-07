FROM excelmicro/base:v1.3.0  
WORKDIR /app  
RUN apt-get install --no-install-recommends -y -q build-essential git ca-
certificates  
RUN mkdir /nodejs && http GET
http://nodejs.org/dist/v4.8.4/node-v4.8.4-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
  
RUN npm install -g forever  
ONBUILD ADD . /app  
ONBUILD RUN (wget --spider -S -T5 -t1 "http://npm.excelmicro.com" 2>&1 | grep
-q "HTTP/" && \  
npm set registry http://npm.excelmicro.com && \  
echo "Using Excel Micro private NPM" || \  
echo "Using public NPM") && \  
npm install --production /app  
  
ADD run.sh /run.sh  
  
RUN chmod 755 /run.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  

