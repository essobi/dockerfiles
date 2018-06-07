FROM progrium/cedarish  
MAINTAINER Eugene Ware <eugene@noblesamurai.com>  
ADD . /buildpack  
ADD ./start.sh /start.sh  
ONBUILD ADD . /app  
ONBUILD WORKDIR /app  
ONBUILD RUN /buildpack/bin/compile /app /tmp  
ONBUILD ENV HOME /app  
ONBUILD ENV PORT 5000  
ONBUILD EXPOSE 5000  
ONBUILD ENTRYPOINT ["/start.sh"]  
ONBUILD CMD ["start", "web"]  

