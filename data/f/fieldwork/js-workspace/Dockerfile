FROM alpine:latest  
  
RUN apk --update add --no-cache --virtual .gyp \  
python \  
make \  
g++ \  
git \  
nodejs \  
nodejs-npm  
  
RUN addgroup -S workspace  
RUN adduser -S workspace -G workspace  
USER workspace  
  
RUN mkdir ~/.npm-global && \  
npm config set prefix '~/.npm-global' && \  
touch ~/.profile && \  
echo "export PATH=~/.npm-global/bin:$PATH" > ~/.profile && \  
source ~/.profile  
  
WORKDIR /workspace  
  
CMD [ "/bin/sh" ]  

