#  
# m3u-scraper Server Dockerfile  
#  
# https://github.com/shuaiscott/docker-m3uscraper  
#  
# Pull base image.  
FROM python:3-alpine  
  
COPY . /usr/src/app/  
  
WORKDIR /usr/src/app/  
  
# Install ffmpeg and required pip packages  
RUN \  
pip install -r ./requirements.txt && \  
rm -rf /var/lib/apt/lists/* && \  
chmod 777 ./updateAndRun.sh  
  
EXPOSE 9009  
CMD [ "./updateAndRun.sh" ]  

