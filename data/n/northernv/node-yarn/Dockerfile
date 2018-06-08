FROM node:8.1  
# Install Yarn Repo  
RUN curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Update and install Yarn  
RUN apt-get update -y && apt-get install yarn  

