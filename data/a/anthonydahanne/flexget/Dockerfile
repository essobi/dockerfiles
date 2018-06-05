FROM python:2.7-onbuild  
MAINTAINER Anthony Dahanne <anthony.dahanne@gmail.com>  
  
# a JS runtime, such as node, is required for cfscrape, see
https://github.com/Anorov/cloudflare-scrape  
RUN apt-get update && apt-get install -y nodejs  
  
# next line not needed since using onbuild + requirements.txt  
#RUN pip install -I flexget transmissionrpc cfscrape  
# this is the current workdir, you may want to attach a volume with config.yml
to instruct flexget what to do  
VOLUME ["/usr/src/app"]  
  
# install the cfscrapper.py plugin  
ADD
https://gist.githubusercontent.com/cvium/8a585b544a98a36434a6/raw/6c3716db58a222ba22015f989e010321dae4a4f8/cfscraper.py
/root/.flexget/plugins/cfscraper.py  
  
# this is the default command, should work fine for most cases, easy to
override anyway  
CMD ["/usr/local/bin/flexget", "--loglevel", "info", "daemon", "start"]  

