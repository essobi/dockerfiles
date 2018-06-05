FROM alpine:3.2  
RUN apk add --update curl jq && rm -rf /var/cache/apk/*  
COPY apply-labels.sh /  
ENTRYPOINT [ "/apply-labels.sh" ]  
CMD [ "" ]  

