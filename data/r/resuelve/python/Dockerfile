FROM alpine:3.7  
LABEL maintainer="rmontesg@resuelve.mx"  
  
ENV PYTHONUNBUFFERED 1  
  
RUN apk --no-cache add -U build-base  
RUN apk --no-cache add -U python python-dev py-pip  
RUN apk --no-cache add -U python3 python3-dev  
  
RUN apk --no-cache add -U postgresql-dev libressl-dev libffi-dev openblas-dev
ffmpeg  
RUN apk --no-cache add ca-certificates  
  
RUN pip3 install pip -U  
RUN pip3 install numpy==1.14.2  
RUN pip3 install pandas==0.22.0  
RUN pip3 install python-dateutil==2.7.2  
RUN pip3 install pytz==2018.3  
RUN pip3 install six==1.11.0  
RUN pip3 install scipy==1.0.0  

