FROM sciruby/iruby-notebook  
  
MAINTAINER Kozo Nishida <knishida@riken.jp>  
  
ADD . /workdir  
WORKDIR /workdir  
  
USER root  
  
RUN gem install specific_install daru statsample rbplotly daru-plotly narray
&& \  
chown -R jovyan:users /workdir  

