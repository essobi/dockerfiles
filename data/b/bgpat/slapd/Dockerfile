FROM alpine:3.7  
RUN apk -U --no-cache add openldap openldap-backend-all && rm
/etc/openldap/slapd.conf  
COPY entrypoint.sh /entrypoint.sh  
  
ENV BACKEND=mdb  
EXPOSE 389 636  
ENTRYPOINT ["/entrypoint.sh"]  

