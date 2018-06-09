FROM s4ysolutions/way-today-runtime  
  
MAINTAINER Sergey Dolin <sergey@s4y.solutions>  
  
RUN mkdir /wt  
COPY package.json /wt/package.json  
  
RUN cd /wt \  
&& npm install  
  
COPY . /wt  
  
RUN cd /wt \  
&& npm run build:server  
  
RUN cd /wt \  
&& npm run build:frontend  
  
RUN cd /wt \  
&& rm -rf docker \  
&& rm -rf src \  
&& rm -rf bin \  
&& rm -rf .git \  
&& rm bitbucket-pipelines.yml .drone.yml .gitignore webpack-* README.md  
  
EXPOSE 80 81 7001  
CMD cd /wt \  
&& npm run start:docker  

