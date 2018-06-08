FROM alpine  
MAINTAINER iaroki  
RUN apk --update --no-cache add python3 \  
&& pip3 --no-cache-dir install pelican Markdown  
RUN adduser -u 1000 -D iaroki  
RUN mkdir /home/iaroki/blog \  
&& chown iaroki:iaroki /home/iaroki/blog  
WORKDIR /home/iaroki/blog  
USER iaroki  
EXPOSE 8000  
ENTRYPOINT ["pelican"]  

