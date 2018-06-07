FROM alpine:3.5  
ENV DUCK_REFRESH 5  
ADD ./update.sh /root/update.sh  
  
RUN apk update;\  
apk add curl;\  
echo "*/$DUCK_REFRESH * * * * sh /root/update.sh >/dev/null 2>&1" >
/etc/crontabs/root;\  
echo "INIT" > /duck.log  
  
CMD sh /root/update.sh ;\  
if grep -vFxq "OK" /duck.log; then \  
echo "Refresh error. DUCK_DOMAIN or DUCK_TOKEN invalid." ;\  
exit ;\  
fi \  
&& crond \  
&& sed -i -e 's/5/'"$DUCK_REFRESH"'/' /etc/crontabs/root \  
&& tail -f /duck.log  

