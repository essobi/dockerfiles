FROM enrico204/minpypy:latest  
  
WORKDIR /opt/app/  
  
ENV TELEGRAM_TOKEN None  
  
RUN useradd -d /opt/app/ -M -U llgbot  
  
RUN apt-get update && apt-get install -y redis-server  
  
COPY requirements.txt ./  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
RUN chown -R llgbot:llgbot /opt/app/  
  
USER llgbot:llgbot  
  
CMD ["pypy", "llgbotapp.py", "--start-redis"]  

