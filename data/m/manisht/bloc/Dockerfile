FROM python:latest  
  
RUN pip install --no-cache-dir -U pip  
  
WORKDIR /app  
COPY setup.py ./  
COPY README.rst ./  
COPY src/ ./src  
  
RUN pip install --no-cache-dir .  
  
EXPOSE 8989  
CMD ["twist", "bloc"]  

