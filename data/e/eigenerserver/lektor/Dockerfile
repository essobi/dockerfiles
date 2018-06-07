FROM eigenerserver/ubuntu:1.0  
LABEL description="Hedgehog Cloud by www.eigener-server.ch
https://www.eigener-server.ch/en/igel-cloud \  
is licensed under a Creative Commons Attribution 4.0 International Lizenz \  
http://creativecommons.org/licenses/by/4.0/ \  
To remove the links visit https://www.eigener-server.ch/en/igel-cloud"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
gcc \  
libffi-dev \  
python2.7 \  
python2.7-dev \  
libssl-dev \  
libffi-dev \  
imagemagick \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
# Fix Let's Encrypt CA not included in Ubuntu's CA bundle  
RUN apt-get update && \  
apt-get -y --no-install-recommends install --reinstall ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/python2.7 /usr/local/bin/python  
  
RUN curl -f https://www.getlektor.com/install.sh | \  
sed 's/sys.stdin/#sys.stdin/' | \  
sed 's/get_confirmation()$/#get_confirmation()/' | \  
sh  
  
RUN git clone https://github.com/eigener-server/lektor-bootstrap.git /project  
  
EXPOSE 5000  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/*  
  
#WORKDIR /host/lektor/project  
ENTRYPOINT ["/bin/bash","/usr/local/bin/run.sh"]  
CMD ["lektor", "server", "--host", "0.0.0.0"]  

