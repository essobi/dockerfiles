FROM alpine:3.3  
ENV AWSCLI_VERSION "1.10.38"  
ENV KMS_DECRYPT_OUT_PATH "/out/secrets.env"  
RUN apk add --update bash groff less python py-pip \  
&& pip install awscli==$AWSCLI_VERSION \  
&& apk --purge -v del py-pip \  
&& rm -rf /var/cache/apk/*  
  
COPY decrypt.sh /usr/bin/  
  
RUN chmod +x /usr/bin/decrypt.sh  
  
ENTRYPOINT "/usr/bin/decrypt.sh"  

