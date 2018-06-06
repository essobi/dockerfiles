FROM node:8.10.0-stretch  
  
RUN apt-get update && apt-get install -y libgconf-2-4 curl xvfb chromium  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser  
  
WORKDIR /usr/src/app  
  
COPY start.sh /usr/src/config/start.sh  
  
ENTRYPOINT ["dumb-init", "--"]  
  
CMD ["/usr/src/config/start.sh"]  

