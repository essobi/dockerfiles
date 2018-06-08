FROM mini/base  
  
ARG AWSEBCLI_VERSION=3.10.2  
RUN apk-install \  
git \  
python3 \  
&& pip3 install --no-cache-dir --upgrade \  
awsebcli==$AWSEBCLI_VERSION \  
&& adduser -D aws  
  
USER aws  
  
VOLUME ["/data"]  
WORKDIR /data  
  
ENTRYPOINT ["eb"]  
CMD ["--help"]  

