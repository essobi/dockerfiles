# Dockerization of Congress:  
#  
# This Docker image will create a minimal environment to run the Congress  
# scrapers in. This provides isolation from the host, and allows testing  
# in an environment that's as close to production as you can.  
#  
#  
# You can build this image by running:  
#  
# docker build --rm -t unitedstates/congress .  
#  
#  
# Running the scraper should be as easy as:  
#  
# export CONGRESS_OUTPUT_DIR=/tmp/congres  
#  
# docker run \  
# -t --rm \  
# -v ${CONGRESS_OUTPUT_DIR}:/congress \  
# unitedstates/congress \  
# ...  
#  
#  
# Where [...] is something like `bills`, or any other arguments to the  
# `run` script.  
#  
# The data produced by the scrape will end up at ${CONGRESS_OUTPUT_DIR}  
# on the host. This path may be any path on the host.  
#  
# One good pattern is to write this out to the /srv/ tree, for example,  
# /srv/pault.ag/congress/ or /srv/io.unitedstates/congress/  
FROM unitedstates/congress  
ADD bill_info_batch.py
/opt/theunitedstates.io/congress/tasks/bill_info_batch.py  
ADD batchrunner.py /opt/theunitedstates.io/congress/batchrunner.py  
  
RUN mkdir -p /data  
WORKDIR /data  
VOLUME /data  

