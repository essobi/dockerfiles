FROM rocketchat/base:4  
  
ENV RC_VERSION develop  
  
RUN mkdir -p /app  
COPY /lib/bundle /app/bundle  
  
RUN set -x \  
&& cd /app/bundle/programs/server \  
&& npm install \  
&& npm cache clear \  
&& chown -R rocketchat:rocketchat /app  
  
USER rocketchat  
  
VOLUME /app/uploads  
  
WORKDIR /app/bundle  
  
EXPOSE 80  
  
CMD ["node", "main.js"]  

