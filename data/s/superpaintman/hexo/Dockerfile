FROM node:5.10.0  
MAINTAINER SuperPaintman <SuperPaintmanDeveloper@gmail.com>  
  
# Install HEXO  
RUN npm install hexo-cli -g  
  
# Workdir  
WORKDIR /app  
VOLUME /app  
  
ENV NODE_ENV production  
ENV NODE_PORT 4000  
ENV HEXO_GENERATE_WATCH true  
  
EXPOSE 4000  
# Entry point  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["hexo", "server"]

