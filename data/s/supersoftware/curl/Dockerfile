FROM alpine  
  
# install curl  
RUN apk --update add curl \  
&& rm -rf /var/cache/apk/*  
  
# output curl's version by default  
ENTRYPOINT ["curl"]  
CMD ["-V"]  

