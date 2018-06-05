FROM python:3-alpine  
  
RUN apk add --no-cache git gcc openjdk8-jre-base wget ca-certificates \  
python3-dev musl-dev linux-headers nano curl net-tools && update-ca-
certificates; \  
wget https://services.gradle.org/distributions/gradle-4.4.1-bin.zip; \  
unzip gradle-4.4.1-bin.zip; rm gradle-4.4.1-bin.zip; \  
export PATH="${PATH}:/gradle-4.4.1/bin"; \  
pip3 install esrally; \  
apk del --purge gcc python3-dev musl-dev linux-headers  
ENV
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/gradle-4.4.1/bin  
COPY rally.ini /root/.rally/rally.ini  
  
ENTRYPOINT [ "esrally"]

