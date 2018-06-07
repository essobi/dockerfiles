FROM python:3.6-slim  
RUN pip install --no-cache-dir aiohttp==3.0.8  
RUN pip install --no-cache-dir click==6.7  
ENTRYPOINT [ "python", "-u", "/app.py" ]  
COPY app.py /app.py  

