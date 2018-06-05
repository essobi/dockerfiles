FROM s4ysolutions/nodejs8x  
  
MAINTAINER Sergey Dolin <sergey@s4y.solutions>  
  
RUN mkdir /s4y  
COPY package.json /s4y/package.json  
RUN cd /s4y && npm install  
  
COPY . /s4y  
  
RUN cd /s4y \  
&& rm -rf docker \  
&& rm -rf bin \  
&& rm -rf .git \  
&& rm -f bitbucket-pipelines.yml .drone.yml .gitignore webpack-* README.md  
  
EXPOSE 80  
CMD cd /s4y && npm run start:docker  

