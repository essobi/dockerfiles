FROM gliderlabs/alpine:3.2  
RUN echo '@alpine-3.1 http://dl-3.alpinelinux.org/alpine/v3.1/main' >>
/etc/apk/repositories \  
&& apk-install nodejs@alpine-3.1 \  
nodejs-dev@alpine-3.1 \  
git \  
python \  
make \  
build-base \  
bash \  
net-tools  
RUN npm install -g codebox \  
&& npm cache clean -g  
  
RUN npm install -g node-gyp &&\  
make clean -C
/usr/lib/node_modules/codebox/node_modules/shux/node_modules/pty.js &&\  
make -C /usr/lib/node_modules/codebox/node_modules/shux/node_modules/pty.js  
  
ENV USER admin  
ENV PASSWD codebox  
  
EXPOSE 8000  
WORKDIR /workspace  
COPY start.sh /start.sh  
CMD ["sh", "/start.sh"]  

