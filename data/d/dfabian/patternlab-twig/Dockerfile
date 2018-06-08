FROM composer  
WORKDIR /app  
  
RUN \  
wget https://github.com/pattern-lab/edition-php-twig-
standard/releases/download/v2.2.1/twig-standard.zip && \  
unzip -d . twig-standard.zip && \  
mv twig-standard/* . && \  
rm -rf twig-standard twig-standard.zip && \  
echo "phpBin: $(which php)" >> ./config/config.yml  
  
ENTRYPOINT ["php", "core/console"]  

