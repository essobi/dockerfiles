# FROM python:3.6.4-slim-jessie  
# RUN mkdir -p /home/dash_app/ \  
# && mkdir -p /home/dash_app/tmp \  
# && mkdir -p /root/.config/matplotlib  
# VOLUME /home/dash_app  
# WORKDIR /home/dash_app  
# COPY . /home/dash_app  
# RUN apt-get update && apt-get install -y gcc \  
# && pip install --no-cache-dir pandas matplotlib \  
# && pip install -r requirements.txt --no-cache-dir \  
# && echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc \  
# && apt-get autoremove --purge -y gcc \  
# && rm -rf /var/lib/apt/lists/*  
FROM drjeckyll/data_science:latest  
  
RUN mkdir -p /home/dash_app/ \  
&& mkdir -p /home/dash_app/tmp  
  
VOLUME /home/dash_app  
WORKDIR /home/dash_app  
COPY . /home/dash_app  
  
EXPOSE 8050  
CMD gunicorn -w 10 -b 0.0.0.0:8050 -t 100000 --max-requests 20 app:server &&
python app.py  

