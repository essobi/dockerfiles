#
# Kibana image
#
FROM 1science/alpine:3.1
# Kibana version
ENV KIBANA_VERSION=4.0.2-linux-x64 KIBANA_HOME=/usr/share/kibana
ENV PATH=${PATH}:${KIBANA_HOME}/bin

# Install NodeJS and Kibana
RUN apk-install nodejs && \
    curl -s https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}.tar.gz | tar zx -C /usr/share && \
    ln -s /usr/share/kibana-${KIBANA_VERSION} $KIBANA_HOME && \
    rm -rf /usr/share/kibana/node && \
    mkdir -p /usr/share/kibana/node/bin && \
    ln -sf /usr/bin/node /usr/share/kibana/node/bin/node && \
    echo -ne "- with Kibana `kibana -V`\n" >> /root/.built

# ADD ./run.sh /usr/local/bin/kibana
# Expose default port
EXPOSE 5601
# Run Kibana in node.js
CMD ["kibana"]



