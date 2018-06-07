FROM ubuntu  
# Will this trigger a build?  
RUN apt-get update -qq && apt-get -q -y install libmysqlclient-dev build-
essential git-core wget libssl-dev  
  
ENV PORT="1337" \  
NODE_ENV="production" \  
NODE_VERSION="4.2.0"  
RUN git clone https://github.com/tj/n.git ~/.n \  
&& cd ~/.n \  
&& make install \  
&& n ${NODE_VERSION} \  
&& rm -rf ~/.n  
RUN npm install -g sails  
RUN mkdir -p /app  
WORKDIR /app  
COPY . /app/  
RUN rm -rf ./node_modules \  
&& npm install --production  
  
EXPOSE 1337  

