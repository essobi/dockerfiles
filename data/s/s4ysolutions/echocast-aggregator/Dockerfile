FROM s4ysolutions/nodejs8x:8.6.0  
# File Author / Maintainer  
MAINTAINER Sergey Dolin <sergey@s4y.solutions>  
  
VOLUME ["/var/lib/ea"]  
  
RUN mkdir /ea  
COPY package.json /ea  
RUN cd /ea \  
&& (test package-lock.json && rm package-lock.json || true) \  
&& npm install --only=production --no-package-lock --loglevel=warn && npm
cache clean --force  
  
COPY . /ea  
EXPOSE 80  
ENV LOG_LEVEL=silly  
ENV DB_LEVEL=verbose  
CMD cd /ea;SQLITE_PATH=/var/lib/echocast-aggregator/db.sqlite npm start  

