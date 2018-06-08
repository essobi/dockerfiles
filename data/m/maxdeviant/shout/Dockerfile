FROM dockerfile/nodejs  
RUN npm install -g shout  
ADD ./defaults/config.js /root/.shout/config.js  
ADD ./users/shout.json /root/.shout/users/shout.json  
EXPOSE 9000  
ENTRYPOINT ["shout"]

