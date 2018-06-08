FROM python:2.7-alpine  
  
MAINTAINER Erlend Finvåg <erlend.finvag@gmail.com>  
  
EXPOSE 8089  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--processes 4", "--workers 2", "--socket :8089"]  
  
RUN apk add -U uwsgi-python curl \  
&& pip install -q flask \  
&& mkdir -p /margarita /var/lock/apache2 /var/run/apache2 \  
&& curl -sSL https://github.com/jessepeterson/margarita/tarball/master \  
| tar zx \  
&& cp -rf jessepeterson-margarita-*/* /margarita \  
&& curl -sSL https://github.com/wdas/reposado/tarball/master | tar zx \  
&& cp -rf wdas-reposado-*/code/reposadolib /margarita \  
&& rm -rf jessepeterson-margarita-* wdas-reposado-* \  
&& adduser -D margarita \  
&& apk del curl \  
&& rm -rf /var/lib/apk/* /tmp/* /var/tmp/*  
  
COPY . /  

