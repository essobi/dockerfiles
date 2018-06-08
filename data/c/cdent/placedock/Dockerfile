FROM alpine:edge  
MAINTAINER Chris Dent <cdent@anticdent.org>  
  
RUN apk add --no-cache python3 python3-dev py3-pip git gcc uwsgi-python3
py3-psycopg2  
# the following are not directly used by placement but are needed by  
# "accidental" imports  
# Used by:  
# netifaces: oslo_utils  
# greenlet: oslo_versionedobjects requires oslo.messaging requires
oslo.service  
# cryptopgraphy: castellan, coming in via nova.conf  
RUN apk add --no-cache py3-netifaces py3-greenlet py-cryptography  
  
# Work around git wanting to know  
RUN git config --global user.email "cdent@anticdent.org" && \  
git config --global user.name "Chris Dent"  
  
# Use a custom requirements file with minimal requirements.  
ADD placement-requirements.txt /  
RUN pip3 install -r placement-requirements.txt  
  
# Do this all in one big piece otherwise the nova bits are out of date  
# Thanks to ingy for figuring out a faster way to do this.  
# We must get rid of a symlink which can lead to errors, see:  
# https://github.com/python/cpython/pull/4267  
RUN git clone \--depth=1 https://git.openstack.org/openstack/nova && \  
cd nova && \  
git fetch --depth=2 --append origin \  
refs/changes/66/362766/101 \  
refs/changes/35/541435/43 \  
refs/changes/57/553857/30 \  
refs/changes/62/543262/22 && \  
git cherry-pick $(cut -f1 .git/FETCH_HEAD) && \  
find . -type l -exec rm {} \; && \  
pip3 install --no-deps .  
  
# add the nova.conf template  
RUN mkdir /etc/nova  
ADD /shared/etc/nova/nova.conf /etc/nova/nova.conf.tmp  
  
# add the tools for creating the placement db  
ADD sync.py /  
  
# add in the uwsgi configuration  
ADD /shared/placement-uwsgi.ini /  
  
# copy in the startup script, which syncs the database and  
# starts uwsgi.  
ADD startup.sh /  
  
CMD ["sh", "-c", "/startup.sh"]  
EXPOSE 80  

