FROM sunix/jekyll4che  
  
ENV CODENVY_APP_BIND_DIR /home/user/app/data  
VOLUME ["/home/user/app/data"]  
  
USER root  
WORKDIR /home/user/app  
  
RUN wget https://github.com/brownbaglunch/BrownBagLunch/archive/gh-pages.zip
&& \  
unzip gh-pages.zip && \  
mv BrownBagLunch-gh-pages/* . && \  
sed -i 's/http:\/\/data.brownbaglunch.fr/data/g' *.html  
  
CMD echo 'url: "http://'$CODENVY_HOSTNAME':'$CODENVY_PORT_4000'"' >>
_config.yml && \  
echo 'baseurl: ""' >> _config.yml && \  
jekyll serve  

