FROM alpine  
copy ["rc", "/root/.cow/rc.temp"]  
RUN apk add --no-cache gettext bash curl  
ENV COW_INSTALLDIR /root  
RUN curl -L git.io/cow | bash  
EXPOSE 7777  
CMD ["/bin/bash","-c", "envsubst < /root/.cow/rc.temp > /root/.cow/rc &&
/root/cow -reply -request -debug"]  

