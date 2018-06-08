FROM python:2  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt \  
&& git clone https://github.com/dav1dde/glad-web.git glad-web  
  
COPY gunicorn.config.py ./glad-web  
COPY gladweb .  
COPY run.sh .  
  
ENV PATH="/usr/src/app:${PATH}"  
EXPOSE 8080  
RUN groupadd -r glad && useradd --no-log-init -r -g glad glad && chown -R
glad:glad ../  
USER glad:glad  
  
CMD ["./run.sh"]  

