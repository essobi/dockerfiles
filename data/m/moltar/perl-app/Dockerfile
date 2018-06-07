FROM moltar/plenv:latest  
  
MAINTAINER moltar <moltar@moltar.net>  
  
ENV APP_DIR /app  
ENV APP_USER app  
  
WORKDIR /app  
  
ADD ./build_perl_project.sh /usr/bin/build_perl_project.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
ONBUILD ADD ./ $APP_DIR  
ONBUILD RUN build_perl_project.sh

