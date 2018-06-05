FROM neilpang/acme.sh  
  
RUN apk update -f \  
&& apk --no-cache add -f \  
python3 \  
bash \  
&& rm -rf /var/cache/apk/* \  
&& pip3 install --upgrade pip  
  
COPY requirements.txt /app/requirements.txt  
RUN pip3 install -r /app/requirements.txt  
  
COPY lets.py /app/lets.py  
ENTRYPOINT []  
CMD python3 /app/lets.py

