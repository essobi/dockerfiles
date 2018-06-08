FROM alpine:3.3  
  
RUN apk add \--update python python-dev py-pip libpq postgresql-dev ca-
certificates netcat-openbsd git openssh bash perl build-base linux-headers
libffi-dev musl-dev \  
&& pip install bumpversion \  
&& apk upgrade \  
&& apk del --purge tar xz curl && rm -Rf /var/cache/apk/*  

