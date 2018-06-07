FROM docker:stable  
  
WORKDIR /app  
  
RUN set -ex \  
&& apk add --no-cache --virtual .run-deps \  
python \  
curl \  
bash \  
openssl-dev \  
&& apk \--no-cache add --virtual .build-deps \  
python2-dev \  
libffi-dev \  
alpine-sdk \  
&& curl https://bootstrap.pypa.io/get-pip.py | python \  
&& curl
https://gist.githubusercontent.com/chrisns/3b10035acac131904bc1d28a80fb02df/raw/d4a63792c4d03d1dd0f77ddfb96f7b48d5c5b7dc/updateSecret.sh
> ./updateSecret.sh \  
&& chmod +x ./updateSecret.sh \  
&& pip install certbot \  
&& apk \--purge del .build-deps \  
&& rm -rf /var/cache/apk/ /root/.cache/pip  
  
ENV PATH=${PATH}:/app  
COPY update-godaddy.sh run.sh ./  
  
ENTRYPOINT []  
CMD ./run.sh  

