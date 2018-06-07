FROM python:2.7-alpine  
  
LABEL net.juniper.ps.automation.description="base python and tornado
installed" \  
net.juniper.ps.automation.maintainer="Paul Plavetzki"  
  
COPY ./requirements.txt /home  
  
RUN apk update \  
&& apk upgrade \  
&& pip install -r /home/requirements.txt \  
&& rm -rf /source/* \  
&& rm -rf /var/cache/apk/*  
  
COPY ./source/ /home/source/  
  
WORKDIR /home/source  
ENV PYTHONPATH="/home"  
EXPOSE 9696  
CMD ["python", "mock_app.py"]

