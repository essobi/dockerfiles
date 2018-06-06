FROM celery  
  
COPY . .  
  
CMD ["celery", "worker", "--app=tasks", "--loglevel=info"]

