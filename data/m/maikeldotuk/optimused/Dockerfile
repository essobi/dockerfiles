FROM python:3.5.4-jessie  
  
# Manually install JQ because problems.  
# (comes without regex support / not 1.5)  
ENV JQ_VERSION='1.5'  
RUN wget --no-check-certificate
https://raw.githubusercontent.com/stedolan/jq/master/sig/jq-release.key -O
/tmp/jq-release.key && \  
wget --no-check-certificate
https://raw.githubusercontent.com/stedolan/jq/master/sig/v${JQ_VERSION}/jq-
linux64.asc -O /tmp/jq-linux64.asc && \  
wget --no-check-certificate
https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64
-O /tmp/jq-linux64 && \  
gpg --import /tmp/jq-release.key && \  
gpg --verify /tmp/jq-linux64.asc /tmp/jq-linux64 && \  
cp /tmp/jq-linux64 /usr/bin/jq && \  
chmod +x /usr/bin/jq && \  
rm -f /tmp/jq-release.key && \  
rm -f /tmp/jq-linux64.asc && \  
rm -f /tmp/jq-linux64  
  
RUN pip install -U pip  
RUN pip install requests  
# Newer versions will break due to  
# what I think is https://github.com/wireservice/csvkit/issues/751  
RUN pip install csvkit==0.9.1  
RUN pip install click  
RUN pip install pyfunctional  
# OK, getting increasingly specific here.  
# This is what you get for trying to make all purpose dockerfiles  
# Really the processes should be split out to just do one thing  
RUN pip install roman  
# More and more wondrous libraries  
RUN pip install pyexcel  
RUN pip install pyexcel-xls  
  
# These are the specifics for gazfeed  
RUN pip install agate  
RUN pip install agate-dbf  
RUN pip install agate-excel  
RUN pip install agate-sql  
RUN pip install Babel  
RUN pip install DateTime  
RUN pip install dbfread  
RUN pip install et-xmlfile  
RUN pip install feedparser  
RUN pip install flatdict  
RUN pip install iso8601  
RUN pip install isodate  
RUN pip install jsonlines  
RUN pip install leather  
RUN pip install parsedatetime  
RUN pip install python-slugify  
RUN pip install pytimeparse  
RUN pip install pytz  
RUN pip install Unidecode  
RUN pip install zope.interface  

