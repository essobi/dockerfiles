FROM alpine  
MAINTAINER Alexander Herrmann <darignac@gmail.com>  
RUN apk update && apk upgrade  
RUN apk add python curl mysql-client  
RUN rm -rf /var/cache/apk/*  
  
RUN adduser -D -u 1000 -g 'bu' bu  
  
WORKDIR /tmp  
  
RUN curl -L -o get-pip.py https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& rm get-pip.py \  
&& pip install python-dateutil python-magic  
  
RUN curl -o s3cmd.zip -L
https://github.com/s3tools/s3cmd/releases/download/v1.6.1/s3cmd-1.6.1.zip \  
&& unzip s3cmd.zip \  
&& mv s3cmd-1.6.1 /usr/local/s3cmd \  
&& rm s3cmd.zip \  
&& ln -s /usr/local/s3cmd/s3cmd /usr/local/bin/s3cmd  
  
ADD backup /home/bu/  
RUN chown bu:bu /home/bu/backup && chmod 700 /home/bu/backup  
  
WORKDIR /home/bu  
USER bu  
ENTRYPOINT ["/home/bu/backup"]  

