FROM python:3-onbuild  
EXPOSE 8080  
  
ENV MONGO_URL "mongodb://localhost:27017/hcstandup"  
ENV REDIS_URL "redis://localhost:6379/hcstandup"  
ENV BASE_URL "https://ngroktunnel.ngrok.com"  
ENV PORT "8080"  
CMD gunicorn app:app -k aiohttp.worker.GunicornWebWorker -b 0.0.0.0:${PORT}  

