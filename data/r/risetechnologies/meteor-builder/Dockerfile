FROM node:8.9.4  
MAINTAINER risetechnologies  
  
RUN curl https://install.meteor.com/?release=1.6.1 | sh \  
&& apt-get update \  
&& apt-get install -y build-essential g++  
  
VOLUME /bundle  
  
ENTRYPOINT cd /app && meteor npm install && meteor npm install --save bcrypt
&& exec "$0" "$@"  
CMD ["meteor", "--unsafe-perm", "build", "--server-only", "--directory",
"/bundle"]  

