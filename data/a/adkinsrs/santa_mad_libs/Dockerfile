FROM alpine  
  
MAINTAINER Shaun Adkins <sadkins@som.umaryland.edu>  
  
EXPOSE 5000  
ENV APP_DIR /app  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.5/main" >>
/etc/apk/repositories \  
&& echo "http://dl-4.alpinelinux.org/alpine/v3.5/community" >>
/etc/apk/repositories  
  
RUN apk update \  
&& apk add python py-pip supervisor \  
&& pip install --upgrade pip \  
&& pip install Flask \  
&& rm -rf /var/cache/apk/*  
  
COPY . ${APP_DIR}  
WORKDIR ${APP_DIR}  
ENTRYPOINT ["python"]  
CMD ["app.py"]  

