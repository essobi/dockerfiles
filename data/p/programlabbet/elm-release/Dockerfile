FROM node:7  
MAINTAINER Anders Hansson <anders@programlabbet.se>  
  
RUN apt-get update -y && apt-get install -y rsync wget unzip && apt-get clean
-y  
RUN npm install -g yarn  
  
RUN yarn global add elm@0.18  
RUN yarn global add elm-github-install  
RUN yarn global add brunch@2.8.2  
RUN yarn global add coffee-script  
  
# Copy script(s)  
COPY build.sh /  
RUN chmod 755 /build.sh  
  
# Volumes (map these for sources)  
VOLUME /src  
WORKDIR /src  
  
# Kick off the building process...  
# (assumes the source is mapped into the /src folder)  
CMD ["/build.sh", "/src"]  

