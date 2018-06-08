from nibirupool/nibiru:latest  
COPY ./blocknotify.c /var/  
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin &&
rm /var/blocknotify.c  
#cloning repo and building daemon  
RUN \  
git clone https://github.com/btcz/bitcoinz.git &&\  
cd bitcoinz && ./zcutil/build.sh  
#running daemon  
RUN \  
/bitcoinz/zcutil/fetch-params.sh &&\  
echo "#!/bin/bash\n/bitcoinz/src/zcashd && bash" > /root/entry.sh &&\  
chmod +x /root/entry.sh  
VOLUME ["/root/.bitcoinz"]  
ENTRYPOINT ["/root/entry.sh"]  
#ENTRYPOINT ["bash"]  

