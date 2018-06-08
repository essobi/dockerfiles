FROM robo2025/python:3.6-alpine  
ENV PYTHONUNBUFFERED 1  
COPY . /project/financialserver  
  
WORKDIR /project/financialserver  
  
RUN pip install -r requirements.txt \  
&& mkdir -p /project/financialserver/logs \  
&& mkdir -p /project/financialserver/media  
  
RUN apk --no-cache add tzdata && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone  
  
CMD ["uwsgi", "/project/financialserver/financial_management/wsgi/uwsgi.ini"]

