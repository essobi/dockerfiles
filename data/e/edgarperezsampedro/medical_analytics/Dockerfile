FROM python:2.7.13-alpine  
MAINTAINER Edgar Perez Sampedro "e.perezsam@alumnos.urjc.com"  
COPY . /app  
WORKDIR /app  
  
RUN apk add --no-cache --virtual=build_dependencies musl-dev gcc python-dev
make cmake g++ gfortran && \  
ln -s /usr/include/locale.h /usr/include/xlocale.h && \  
pip install numpy && \  
pip install pandas==0.18.1 && \  
apk del build_dependencies && \  
apk add --no-cache libstdc++ && \  
rm -rf /var/cache/apk/*  
  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python"]  
CMD ["medical_analytics.py"]  
EXPOSE 5000  

