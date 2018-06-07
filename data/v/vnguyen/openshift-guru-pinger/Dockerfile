FROM centos:centos7  
  
ENV APP_HOME=/usr/src/app/  
WORKDIR $APP_HOME  
RUN yum install -y bind-utils traceroute \  
&& yum clean all \  
&& curl -O https://nodejs.org/dist/v6.10.3/node-v6.10.3-linux-x64.tar.xz \  
&& tar --strip-components 1 -xvf node-v* -C /usr/local \  
&& rm -f node-v*  
  
COPY app.js package.json $APP_HOME  
RUN cd $APP_HOME \  
&& npm install  
  
CMD ["npm", "start"]  

