#Dockerfile for zclassic daemon.  
FROM nibirupool/nibiru:latest  
RUN \  
git clone https://github.com/z-classic/zclassic.git &&\  
cd zclassic &&\  
./zcutil/build.sh &&\  
./zcutil/fetch-params.sh  
COPY ./blocknotify.c /var/  
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin &&
rm /var/blocknotify.c  
RUN \  
mkdir /root/.zclassic  
RUN \  
echo "#!/bin/bash\n/zclassic/src/zcashd && bash" > /root/entry.sh &&\  
chmod +x /root/entry.sh  
VOLUME ["/root/.zclassic"]  
ADD ./zclassic.conf /root/.zclassic/zclassic.conf  
ENTRYPOINT ["/root/entry.sh"]  

