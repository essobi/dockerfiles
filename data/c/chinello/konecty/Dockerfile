FROM node:4.8  
ENV KONECTY_VERSION 0.5.3  
RUN set -x \  
&& curl -SLf
"https://github.com/sampaiodiego/konecty/releases/download/$KONECTY_VERSION/konecty.tar.gz"
-o konecty.tar.gz \  
&& mkdir /app \  
&& tar -zxf konecty.tar.gz -C /app \  
&& rm konecty.tar.gz \  
&& cd /app/bundle/programs/server/ \  
&& npm install \  
&& npm cache clear  
  
WORKDIR /app/bundle  
  
ENV PORT=3000 \  
ROOT_URL=http://localhost:3000  
EXPOSE 3000  
CMD ["node", "main.js"]  

