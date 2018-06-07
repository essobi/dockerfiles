FROM alpine:edge  
  
MAINTAINER JAremko <w3techplaygound@gmail.com>  
  
RUN apk --no-cache add --virtual build-deps \  
build-base \  
gettext-dev \  
git \  
py-setuptools \  
py2-pip \  
python2-dev \  
&& apk --no-cache add \  
gettext \  
py2-certifi \  
py2-chardet \  
py2-idna \  
py2-requests \  
py2-urllib3 \  
python2 \  
## && pip install git+https://github.com/linkcheck/linkchecker \  
&& pip install git+https://github.com/JAremko/linkchecker \  
&& apk del build-deps  
  
COPY linkcheckerrc /root/.linkchecker/linkcheckerrc  
  
ENTRYPOINT ["linkchecker"]  
  

