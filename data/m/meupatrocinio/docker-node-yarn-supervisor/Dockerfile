FROM alpine  
  
  
WORKDIR /var/www/  
VOLUME ["/var/www/"]  
RUN echo -e 'http://dl-cdn.alpinelinux.org/alpine/edge/main\nhttp://dl-
cdn.alpinelinux.org/alpine/edge/community\nhttp://dl-
cdn.alpinelinux.org/alpine/edge/testing' > /etc/apk/repositories  
RUN apk add --no-cache nodejs openssl bash yarn python3-dev \  
&& yarn global add supervisor nodemon  
  
RUN ln -sf /usr/bin/python3 /usr/bin/python  
  
COPY run.sh /run.sh  
  
CMD ["/run.sh"]  
  
ENV SUPERVISOR="" \  
SUPERVISORFLAGS=""  
EXPOSE 8890  

