FROM alpine:3.6  
LABEL authors="Hazim <hazim_malik@hotmail.com>"  
  
RUN apk --no-cache add --update bash  
ADD ./dumb-exit.sh /dumb-exit.sh  
CMD ["/dumb-exit.sh"]  

