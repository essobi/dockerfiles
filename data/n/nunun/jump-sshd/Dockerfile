FROM alpine  
WORKDIR /  
RUN apk -U upgrade \  
&& apk --no-cache add openssh bash curl mysql-client tzdata \  
&& rm -rf /var/cache/apk/*  
ADD start.sh /  
CMD sh /start.sh  

