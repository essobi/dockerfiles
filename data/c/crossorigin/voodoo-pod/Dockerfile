FROM gliderlabs/herokuish  
  
RUN apt-get update > /dev/null && \  
apt-get install -y python-pip > /dev/null && \  
pip install shyaml > /dev/null && \  
rm -R -f /tmp/buildpacks/heroku-buildpack-nodejs && \  
/bin/herokuish buildpack install https://github.com/heroku/heroku-buildpack-
nodejs.git  
  
COPY entrypoint.sh /bin/  
  
ENTRYPOINT ["/bin/entrypoint.sh"]

