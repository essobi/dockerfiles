FROM python:3-alpine  
  
RUN pip install itchat  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps openssl \  
# https://gist.github.com/littlecodersh/e93532d5e7ddf0ec56c336499165c4dc  
&& wget -O $(python -c "import site;
print(site.getsitepackages()[0])")/requests/packages/urllib3/fields.py \  
https://gist.githubusercontent.com/littlecodersh/e93532d5e7ddf0ec56c336499165c4dc/raw/9ef4f11c7dca8f3e0c8fa4b32482cbe20e458668/fields.py
\  
&& apk del .fetch-deps  
  
VOLUME ["/app"]  
WORKDIR /app  
CMD ["python", "main.py"]  

