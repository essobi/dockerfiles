FROM docker:latest  
RUN apk -v --update add \  
zip \  
python \  
py-pip \  
groff \  
less \  
mailcap \  
git \  
bash \  
&& \  
pip install --upgrade awscli s3cmd python-magic && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
VOLUME /root/.aws  
VOLUME /project  
WORKDIR /project  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["bash"]  
  

