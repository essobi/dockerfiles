FROM golang:onbuild  
EXPOSE 10100  
EXPOSE 10101  
VOLUME /etc/redirect  
CMD ["app", "-config", "/etc/redirect/config.json", "-ui", "/go/src/app/ui",
"-ui-addr", "0.0.0.0:10101"]  

