FROM node:8.9.4  
  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends git xvfb libgtk2.0-0 libnotify-dev
libgconf-2-4 libnss3 libxss1 libasound2 zip && \  
yarn global add create-react-app cypress graphql-faker && \  
cypress install  

