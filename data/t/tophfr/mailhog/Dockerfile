FROM alpine:3.7  
MAINTAINER toph <toph@toph.fr>  
  
RUN apk add --no-cache ca-certificates openssl  
RUN mkdir -p /usr/local/sbin  
  
ARG MAILHOG_VERSION=1.0.0  
RUN wget
"https://github.com/mailhog/MailHog/releases/download/v$MAILHOG_VERSION/MailHog_linux_amd64"
-O /usr/local/sbin/mailhog \  
&& chmod a+x /usr/local/sbin/mailhog  
  
ENV MH_API_BIND_ADDR :80  
ENV MH_UI_BIND_ADDR :80  
ENV MH_SMTP_BIND_ADDR :25  
EXPOSE 25 80  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["mailhog"]  

