FROM python:3-alpine  
  
ENV HOST https://HOST  
ENV API /api  
ENV BOT_NAME_EN CloudMusicBot  
ENV BOT_NAME_TW 網易雲音樂解析  
ENV LOGCHANNELID ID  
ENV TOKEN YOUR_TOKEN  
ENV IP 0.0.0.0  
ENV PORT 8080  
ADD *.py /bot/  
ADD requirements.txt /bot/  
ADD _config.yml /bot/  
  
WORKDIR /bot  
  
RUN apk add --no-cache gcc musl-dev  
RUN apk add --no-cache g++  
RUN pip install -r ./requirements.txt  
RUN apk del gcc musl-dev g++  
  
CMD ["python", "./app.py"]  
  
EXPOSE 8080  

