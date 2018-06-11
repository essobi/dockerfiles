FROM needleops/python  
  
COPY . /app  
RUN apk add --update libzmq python3-dev build-base libxml2 libxml2-dev libxslt
libxslt-dev \  
&& /env/bin/pip install --no-use-wheel -r /app/requirements.txt \  
&& apk del python3-dev build-base libxml2-dev libxslt-dev --purge  
  
EXPOSE 8080  
CMD ["/env/bin/python", "-m wolverine.web"]  

