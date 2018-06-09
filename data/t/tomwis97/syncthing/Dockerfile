FROM alpine:latest  
RUN adduser -D syncthinguser && \  
apk update && \  
apk add openssl ca-certificates bash  
USER syncthinguser  
RUN cd ~ && \  
wget `wget -qO-
https://api.github.com/repos/syncthing/syncthing/releases/latest | grep linux-
amd64 | grep browser_download_url | cut -d '"' -f4` && \  
tar xvf syncthing-linux-amd64* && \  
rm *tar.gz && \  
mv syncthing* syncthing && \  
mkdir .config/syncthing -p  
VOLUME /mnt  
VOLUME /home/syncthinguser/.config/syncthing  
EXPOSE 8384 22000 21027/udp  
CMD /home/syncthinguser/syncthing/syncthing -gui-
address="https://0.0.0.0:8384"  

