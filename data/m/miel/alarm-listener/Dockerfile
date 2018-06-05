FROM python:3-alpine  
LABEL maintainer="Miel Donkers"  
  
# Some additional Alpine packages  
RUN apk --update add --no-cache tzdata su-exec openssl ca-certificates py-
openssl  
RUN apk --update add --virtual .build-dependencies libffi-dev openssl-dev
python-dev build-base  
  
# Set the timezone, Alpine style...  
RUN cp /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime  
RUN echo "Europe/Amsterdam" > /etc/timezone  
RUN apk del tzdata  
  
## Set the working directory to Python app directory  
WORKDIR /usr/src/app  
  
# Install the app  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
RUN apk del .build-dependencies  
  
COPY alarmlistener ./alarmlistener/  
  
# Create directory, a user and group used to launch processes  
RUN addgroup alarm \  
&& adduser -s /bin/sh -h /usr/src/app -D -G alarm alarm \  
&& chown -R alarm:alarm /usr/src/app  
  
# Expose port  
EXPOSE 32001  
# VOLUME /usr/src/app  
# VOLUME /tmp  
# Run command  
CMD ["su-exec", "alarm", "sh", "-c", "python3 -m alarmlistener"]  
  

