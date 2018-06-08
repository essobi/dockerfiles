FROM java:7-jre  
  
ENV BAMBOO_VERSION 5.7.2  
ENV BAMBOO_DOWNLOAD_URL
http://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-$BAMBOO_VERSION.tar.gz  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends git subversion mercurial ssh-
client \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /opt/bamboo \  
&& mkdir -p /home/bamboo \  
&& curl -sSL $BAMBOO_DOWNLOAD_URL -o /tmp/bamboo.tar.gz \  
&& tar -xzf /tmp/bamboo.tar.gz -C /opt/bamboo --strip-components=1 \  
&& rm /tmp/bamboo.tar.gz \  
&& ( echo "bamboo.home=/home/bamboo" | tee -a /opt/bamboo/atlassian-
bamboo/WEB-INF/classes/bamboo-init.properties )  
  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME /home/bamboo  
EXPOSE 8085 54663  
  
WORKDIR /home/bamboo  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bamboo"]  

