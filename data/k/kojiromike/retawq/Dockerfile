FROM alpine  
ENV RETAWQ_VERSION=0.2.6c  
ENV RETAWQ_MD5=ee60188bea597680bd39e435a8c73ff9  
ENV RETAWQ=retawq-$RETAWQ_VERSION  
ENV
RETAWQ_URL=http://downloads.sourceforge.net/project/retawq/retawq/$RETAWQ/$RETAWQ.tar.gz  
RUN apk update \  
&& apk add build-base \  
wget \  
ncurses-dev \  
openssl-dev \  
&& wget -O "/tmp/$RETAWQ.tar.gz" "$RETAWQ_URL" \  
&& cd /tmp \  
&& echo "$RETAWQ_MD5 *$RETAWQ.tar.gz" | md5sum -c \  
&& tar -xzf "$RETAWQ.tar.gz" \  
&& cd "$RETAWQ" \  
&& ./configure --set-tls=2 \  
&& make \  
&& make install \  
&& cd \  
&& rm -rf /tmp/$RETAWQ-*  
ENTRYPOINT ["retawq"]  

