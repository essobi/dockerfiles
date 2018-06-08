# Builds the Bash Test Runner image  
# escape=\  
FROM alpine:3.7  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
## Install dependencies  
RUN apk add --update bash run-parts \  
curl \  
&& rm -rf /var/cache/apk/* \  
&& curl https://codeload.github.com/kward/shunit2/tar.gz/v2.1.7 -o
shunit2.tar.gz \  
&& tar -xvf shunit2.tar.gz \  
&& mv shunit2-2.1.7 /bin/shunit2 \  
&& rm *.gz \  
&& ln -s /bin/shunit2/shunit2 /usr/sbin/shunit2  
  
WORKDIR /test  
  
ENTRYPOINT [ "sh" , "-c" ]  
  
CMD [ "for file in `ls test_*.sh`; do ./$file ;done" ]  

