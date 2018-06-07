# Install Polymer CLI, https://www.polymer-project.org/1.0/start/first-
element/intro  
FROM node:6-slim  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists/*  
RUN npm install -g bower polymer-cli  
EXPOSE 5000  
# Create app directory  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
CMD ["bower", "install"]  
CMD ["polymer", "serve", "--hostname", "0.0.0.0"]

