FROM nginx  
  
MAINTAINER Joe Black <joe@valuphone.com>  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 /dumb-init  
RUN chmod +x /dumb-init  
  
RUN apt-get update -qq && apt-get install --no-install-recommends --no-
install-suggests -yqq curl ca-certificates python3 python3-lxml && apt-get
clean && rm -rf /var/lib/apt/lists/*  
RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python3  
RUN pip3 install tmpld  
  
RUN rm -f /etc/nginx/conf.d/default.conf  
COPY conf/nginx.conf /etc/nginx/  
COPY conf/server-avas.conf /etc/nginx/conf.d/  
COPY conf/.htpasswd /etc/nginx/  
  
COPY templates /templates  
  
COPY entrypoint /  
  
ENV TMPLD_EXTENSIONS=  
ENV TMPLD_LOG_LEVEL=warning  
  
ENTRYPOINT ["/dumb-init", "--"]  
CMD ["/entrypoint"]  

