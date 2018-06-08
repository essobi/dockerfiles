FROM nvidia/cuda:9.1-base  
  
COPY root /  
  
RUN adduser --system --disabled-password --no-create-home --home /xmrig-nvidia
xmrig && \  
apt-get update && \  
apt-get install -y --no-install-recommends libuv1 libmicrohttpd10 && \  
rm -rf /var/cache/apk/*  
  
USER xmrig  
  
WORKDIR /xmrig-nvidia  
  
ENTRYPOINT [ "./xmrig-nvidia" ]  
CMD [ "--help" ]  

