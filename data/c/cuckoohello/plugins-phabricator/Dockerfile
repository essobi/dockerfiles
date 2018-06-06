FROM alpine:3.7  
RUN apk add --no-cache git php7 php7-curl php7-json bash  
  
RUN mkdir -p ~/phacility && cd ~/phacility && git clone
https://github.com/phacility/libphutil.git -b stable --depth=1 && git clone
https://github.com/phacility/arcanist.git -b stable --depth=1  
  
COPY script.sh /bin/script.sh  
  
ENTRYPOINT /bin/script.sh  

