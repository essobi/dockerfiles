FROM composer:latest  
  
RUN export PATH="`composer config --global data-dir`/`composer config --global
bin-dir`:$PATH" \  
&& composer global require hirak/prestissimo  

