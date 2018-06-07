FROM ghost:0.7.1  
MAINTAINER Marcel Kilian <cdskilian@gmail.com>  
  
# Add in better default config adapted from
https://github.com/kitematic/ghost.git  
ADD config.example.js config.example.js  
  
# use custom entrypoint script  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# Fix ownership in src  
RUN chown -R user $GHOST_SOURCE/content && chmod +x /entrypoint.sh  
  
# Default environment variables  
ENV GHOST_URL http://my-ghost-blog.com  

