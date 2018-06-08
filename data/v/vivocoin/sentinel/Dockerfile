FROM alpine:latest as build  
WORKDIR /root/build  
RUN apk update && \  
apk add \  
git \  
py2-pip && \  
pip install \  
inflection==0.3.1 \  
peewee==2.8.3 \  
python-bitcoinrpc==1.0 && \  
git clone https://github.com/vivocoin/sentinel && \  
cd sentinel && \  
rm -rf \  
test \  
share \  
.git \  
.gitattributes \  
.gitignore \  
.travis.yml \  
LICENSE \  
README.md \  
requirements.txt \  
sentinel.conf \  
bin/dbtest.py \  
bin/dehex.py \  
bin/rehex.py  
  
FROM alpine:latest as assemble  
RUN apk update && \  
apk --no-cache add \  
py2-py \  
py2-simplejson && \  
adduser -s /bin/false -D vivo  
WORKDIR /opt/wallet/vivo/sentinel  
COPY --from=build /root/build/sentinel ./  
COPY --from=build \  
/usr/lib/python2.7/site-packages/inflection.pyc \  
/usr/lib/python2.7/site-packages/peewee.pyc \  
/usr/lib/python2.7/site-packages/  
COPY --from=build \  
/usr/lib/python2.7/site-packages/bitcoinrpc \  
/usr/lib/python2.7/site-packages/bitcoinrpc  
COPY --from=build \  
/usr/lib/python2.7/site-packages/playhouse \  
/usr/lib/python2.7/site-packages/playhouse  
COPY crontab ./  
COPY init.sh bootstrap.sh ./  
RUN chmod 755 init.sh bootstrap.sh && \  
chmod 644 crontab  
  
FROM scratch  
COPY --from=assemble / /  
RUN chown vivo:vivo -R /home/vivo  
ENV SECRET_OVERRIDE=0 VIVO_RPCUSER=vivo VIVO_RCPPASSWORD=vivo
VIVO_HOSTNAME=vivod  
ENTRYPOINT [ "/opt/wallet/vivo/sentinel/init.sh" ]  

