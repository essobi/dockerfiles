FROM node:slim  
  
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ git
libc-dev make python && \  
mkdir -p /app  
  
WORKDIR /app  
  
RUN git clone https://github.com/DeviaVir/zenbot . && \  
npm install  
  
VOLUME ["/app/conf.js"]  
  
CMD ["./zenbot.sh"]  

