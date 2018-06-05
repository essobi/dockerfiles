FROM baden/debian  
MAINTAINER Denys Batrak baden.i.ua@gmail.com  
  
ENV DEBIAN_FRONTEND="noninteractive"  
# LTS  
ENV NODE_VERSION=4.5.0  
RUN apt-get update -qq && \  
apt-get install -y xz-utils inotify-tools && \  
apt-get -qq clean  
  
RUN mkdir /node && \  
cd /node && \  
curl -O
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz
&& \  
tar xf ./node-v${NODE_VERSION}-linux-x64.tar.xz && \  
rm ./node-v${NODE_VERSION}-linux-x64.tar.xz  
  
ENV PATH /node/node-v${NODE_VERSION}-linux-x64/bin/:${PATH}  
  
RUN npm install -g grunt-cli bower -q  
  
# root entrypoint  
RUN mkdir /app  
WORKDIR /app  
  
# Install some for user composer  
RUN USER_ID=1000 GROUP_ID=1000 /entrypoint.sh true  
  
ARG PORT=4000  
ENV PORT=${PORT}  
  
EXPOSE ${PORT}  
  
CMD ["bash"]  

