FROM ubuntu:latest  
  
ENV RICTY_URL http://www.rs.tus.ac.jp/yyusa/ricty  
ENV RICTY_VERSION 4.1.1  
ENV MIGU_VERSION 20150712  
ENV MIGU_RELEASE_ID 63545  
RUN apt-get update \  
&& apt-get install -y curl zip unzip fontforge-nox fonttools \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /Ricty  
  
RUN mkdir -p LICENSE LICENSE/Migu LICENSE/Inconsolata \  
&& curl -o ricty_generator.sh -SL
${RICTY_URL}/ricty_generator-${RICTY_VERSION}.sh \  
&& chmod +x *.sh \  
&& curl -o migu.zip -SL http://osdn.jp/frs/redir.php?f=%2Fmix-mplus-
ipa%2F${MIGU_RELEASE_ID}%2Fmigu-1m-${MIGU_VERSION}.zip \  
&& unzip migu.zip && rm migu.zip \  
&& mv migu-1m-${MIGU_VERSION}/* . \  
&& mv ipag* mplus* migu-README.txt LICENSE/Migu \  
&& rm -r migu-1m-${MIGU_VERSION} \  
&& curl -o Inconsolata-Regular.ttf -SL
https://github.com/google/fonts/raw/master/ofl/inconsolata/Inconsolata-
Regular.ttf \  
&& curl -o Inconsolata-Bold.ttf -SL
https://github.com/google/fonts/raw/master/ofl/inconsolata/Inconsolata-
Bold.ttf \  
&& curl -o LICENSE/Inconsolata/OFL.txt -SL
https://github.com/google/fonts/raw/master/ofl/inconsolata/OFL.txt  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

