FROM codeworksio/python:3.6-20180210  
  
ENV SPEEDTEST_INTERVAL="1200"  
  
RUN set -ex; \  
\  
SPEEDTEST_CLI_VERSION="2.0.0"; \  
\  
curl -L https://github.com/sivel/speedtest-
cli/archive/v${SPEEDTEST_CLI_VERSION}.tar.gz -o speedtest-cli.tar.gz; \  
tar -xvzf speedtest-cli.tar.gz -C /usr/local; \  
mv /usr/local/speedtest-cli-$SPEEDTEST_CLI_VERSION /usr/local/speedtest-cli; \  
chmod +x /usr/local/speedtest-cli/speedtest.py; \  
rm speedtest-cli.tar.gz; \  
\  
pip install \  
pytz  
  
COPY assets/ /  
  
CMD [ "/usr/local/bin/speedtest.py" ]  
  
### METADATA
###################################################################  
  
ARG IMAGE  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
org.label-schema.name=$IMAGE \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.schema-version="1.0"  

