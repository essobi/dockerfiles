FROM semtech/mu-cl-resources:1.16.0  
COPY . /app/dependencies/resources-generator/  
ADD ./startup.lisp /usr/src/startup.lisp  
  
CMD sh /load-config.sh; sbcl --load /usr/src/startup.lisp  

