FROM alpine:3.6  
RUN apk add --no-cache git screen gcc musl-dev nano openssl build-base bash
netcat-openbsd curl  
RUN git clone https://github.com/robertdavidgraham/telnetlogger.git  
WORKDIR /telnetlogger/  
RUN gcc telnetlogger.c -o telnetlogger -lpthread  
RUN rm ips.txt && rm passwords.txt  
RUN touch ips.txt && touch passwords.txt  
RUN mv telnetlogger /bin/telnetlogger  
EXPOSE 23  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 777 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

