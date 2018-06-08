FROM python:3.4-slim  
  
RUN mkdir -p /app && \  
adduser --system verifier  
  
COPY requirements.txt /app/  
RUN pip install -r /app/requirements.txt  
  
COPY codeverifier /app/codeverifier  
COPY verify runner /app/  
RUN chmod +x /app/verify && \  
chmod +x /app/runner && \  
python3 -m compileall /app/codeverifier  
  
USER verifier  
ENV PATH="$PATH:/app"  

