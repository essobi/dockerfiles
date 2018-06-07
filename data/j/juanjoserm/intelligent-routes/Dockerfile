FROM python:3  
WORKDIR /opt  
  
RUN pip install flask requests wasp-eureka mysql-connector python-jose pytest
pytest-allure-adaptor  
  
COPY Controller_Routes.py /opt/  
COPY UrlParse.py /opt/  
COPY forecast.py /opt/  
COPY forecast_datetime.json /opt/  
COPY multipoligono.json /opt/  
  
EXPOSE 5001  
CMD python3 ./Controller_Routes.py

