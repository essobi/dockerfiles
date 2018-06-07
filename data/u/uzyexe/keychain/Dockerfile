FROM alpine:3.4  
RUN apk add --update make python-dev py-pip ruby ruby-dev gcc musl-dev git ca-
certificates && \  
pip install Flask==0.9 requests==0.14.1 boto==2.6.0 eventlet==0.9.17 && \  
gem install io-console foreman --no-ri --no-rdoc && \  
git clone https://github.com/progrium/keychain.io.git && \  
apk del --purge make git gcc musl-dev py-pip && \  
rm -rf /var/cache/apk/*  
  
ENV AWS_ACCESS_KEY_ID **YOUR_AWS_ACCESS_KEY_ID**  
ENV AWS_SECRET_ACCESS_KEY **YOUR_AWS_SECRET_ACCESS_KEY**  
ENV SENDGRID_USERNAME **YOUR_SENDGRID_USERNAME**  
ENV SENDGRID_PASSWORD **YOUR_SENDGRID_PASSWORD**  
ENV KEYCHAIN_BUCKET_NAME **YOUR_KEYCHAIN_BUCKET_NAME**  
  
ENTRYPOINT ["/usr/bin/foreman"]  
CMD ["start", "-d", "/keychain.io"]  
  
EXPOSE 5000  

