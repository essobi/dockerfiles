FROM ubuntu:14.04.4  
MAINTAINER github.com/PengBAI  
  
ENV SHARELATEX_VERSION 0.2.0  
ENV SHARELATEX_HOME /sharelatex  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm texlive-full curl git vim  
RUN apt-get install -y aspell aspell-en aspell-af aspell-am aspell-ar aspell-
ar-large aspell-bg aspell-bn aspell-br aspell-ca aspell-cs aspell-cy aspell-da
aspell-de aspell-de-alt aspell-el aspell-eo aspell-es aspell-et aspell-eu-es
aspell-fa aspell-fo aspell-fr aspell-ga aspell-gl-minimos aspell-gu aspell-he
aspell-hi aspell-hr aspell-hsb aspell-hu aspell-hy aspell-id aspell-is aspell-
it aspell-kk aspell-kn aspell-ku aspell-lt aspell-lv aspell-ml aspell-mr
aspell-nl aspell-no aspell-nr aspell-ns aspell-or aspell-pa aspell-pl aspell-
pt-br aspell-ro aspell-ru aspell-sk aspell-sl aspell-ss aspell-st aspell-sv
aspell-ta aspell-te aspell-tl aspell-tn aspell-ts aspell-uk aspell-uz aspell-
xh aspell-zu  
RUN apt-get install -y --force-yes mongodb-server redis-server wget time  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN curl -o /tmp/sharelatex.tar.gz -SL
https://github.com/sharelatex/sharelatex/archive/v$SHARELATEX_VERSION.tar.gz;
\  
mkdir -p $SHARELATEX_HOME; \  
tar -xzf /tmp/sharelatex.tar.gz --strip-components=1 -C $SHARELATEX_HOME; \  
rm -f /tmp/sharelatex.tar.gz; \  
cd $SHARELATEX_HOME; \  
npm install; \  
npm install -g grunt-cli; \  
grunt install;  
  
ADD sharelatex.sh /sharelatex.sh  
ADD settings.development.coffee /etc/sharelatex/settings.coffee  
  
RUN chmod +x /sharelatex.sh  
  
EXPOSE 3000  
CMD /sharelatex.sh

