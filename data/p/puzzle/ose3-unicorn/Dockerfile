FROM puzzle/ose3-unicorn  
  
ONBUILD COPY . /opt/app-root/src  
ONBUILD RUN scl enable rh-ruby23 "bundle install --path .bundle"  

