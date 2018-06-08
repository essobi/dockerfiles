# Install Polymer CLI, https://www.polymer-project.org/2.0/docs/tools/polymer-
cli  
FROM node  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g bower polymer-cli --unsafe-perm  
  
EXPOSE 8080  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
CMD ["polymer", "serve"]  

