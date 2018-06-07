#Dockerfile for hush daemon.  
from nibirupool/nibiru:latest  
RUN \  
git clone https://github.com/MyHush/hush.git &&\  
cd hush &&\  
./zcutil/fetch-params.sh &&\  
./zcutil/build.sh  
COPY ./blocknotify.c /var/  
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin &&
rm /var/blocknotify.c  
RUN \  
mkdir /root/.hush  
RUN \  
echo "#!/bin/bash\n/hush/src/hushd && bash" > /root/entry.sh &&\  
chmod +x /root/entry.sh  
VOLUME ["/root/.hush"]  
ADD ./hush.conf /root/.hush/hush.conf  
ENTRYPOINT ["/root/entry.sh"]  

