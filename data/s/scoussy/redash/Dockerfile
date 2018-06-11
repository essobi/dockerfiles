FROM redash/redash:4.0.0.b3387  
  
USER root  
  
RUN pip install Jinja2==2.10 deepstreamio_client  
  
COPY . ./  
RUN npm install && npm run build && rm -rf node_modules  
RUN chown -R redash /app  
  
USER redash  

