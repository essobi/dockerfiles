FROM python:3.6.5-alpine3.4  
RUN apk add --no-cache git && \  
pip install pipenv && \  
mkdir -p /app && \  
git clone https://github.com/visheyra/kv-pusher.git /app  
  
WORKDIR /app  
  
RUN pipenv install --system  
  
ENTRYPOINT ["python", "/app/app/app.py"]

