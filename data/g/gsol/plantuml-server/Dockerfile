FROM gsol/plantuml-server:v1.2018.1  
  
MAINTAINER Global-solutions  
  
ENV LC_LANG=ja-JP  
COPY fonts.conf /root/.config/fontconfig/  
  
# IPA Font's license is under the WORKDIR  
  
RUN apk --update add --no-cache --virtual .deps ca-certificates wget openssl
&& \  
update-ca-certificates && \  
mkdir /tmp/work -p && cd /tmp/work && \  
wget http://ipafont.ipa.go.jp/old/ipafont/ipag00303.php -O ipag00303.zip && \  
unzip ipag00303.zip && \  
mkdir /root/.local/share/fonts -p && \  
mv ipag00303/ipag.ttf /root/.local/share/fonts && \  
mv ipag00303/IPA_Font_License_Agreement_v1.0.txt $OLDPWD/ && \  
cd $OLDPWD && \  
rm /tmp/work -rf && \  
apk del .deps  

