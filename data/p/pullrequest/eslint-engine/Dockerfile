FROM python:alpine  
  
# Install eslint  
RUN apk add --update nodejs  
RUN npm install -g eslint eslint-plugin-react babel-eslint  
  
COPY app /app  
  
RUN adduser -u 5000 app -D  
RUN chown -R app:app /app  
  
USER app  
  
WORKDIR /code  
  
CMD python /app/run.py  

