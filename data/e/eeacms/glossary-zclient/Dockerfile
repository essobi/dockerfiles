FROM eeacms/zope:2.8.0  
MAINTAINER "EEA: IDM2 A-Team" <eea-edw-a-team-alerts@googlegroups.com>  
  
# Path to zope instance  
ENV ZOPE_INSTANCE /var/local/zclient  
ENV ZOPE_USER zope  
RUN groupadd -g 500 zope && \  
useradd zope -g zope && \  
usermod -u 500 zope && \  
  
# Create zope instance  
python $ZOPE_PATH/bin/mkzopeinstance.py -d $ZOPE_INSTANCE -u
$ZOPE_USER:$ZOPE_USER && \  
touch $ZOPE_INSTANCE/log/event.log  
  
# Configuration  
RUN chown -R zope:zope $ZOPE_INSTANCE  
COPY zope.conf $ZOPE_INSTANCE/etc/zope.conf  
  
# Adding application code  
## install dependencies  
RUN yum -y updateinfo && yum -y install git && \  
  
## Install pygoogle  
wget https://pypi.python.org/packages/source/p/pygoogle/pygoogle-0.6.tar.gz &&
\  
tar xvf pygoogle-0.6.tar.gz && \  
cd pygoogle-0.6/ && python2.3 setup.py install && cd .. && \  
  
## Install itools-0.9.5  
yum -y install unzip && \  
wget https://github.com/hforge/itools/archive/0.9.5.zip -O itools-0.9.5.zip &&
\  
unzip itools-0.9.5.zip && \  
echo "Revision: \n Version 1.0.0" > itools-0.9.5/Changelog && \  
cd itools-0.9.5/ && python2.3 setup.py install && cd .. && \  
rm -rf pygoogle-0.6* itools-0.9.5* && yum clean all  
  
USER zope  
  
## get the application code  
RUN git clone https://github.com/eea/EEAGlossary.git
$ZOPE_INSTANCE/Products/EEAGlossary && \  
git clone https://github.com/eea/ALiSS_agents.git $ZOPE_INSTANCE/ALiSS_agents
&& \  
ln -s $ZOPE_INSTANCE/ALiSS_agents/ALiSS $ZOPE_INSTANCE/Products/ALiSS && \  
ln -s $ZOPE_INSTANCE/ALiSS_agents/EEAALiSS $ZOPE_INSTANCE/Products/EEAALiSS &&
\  
ln -s $ZOPE_INSTANCE/ALiSS_agents/Localizer $ZOPE_INSTANCE/Products/Localizer
&& \  
ln -s $ZOPE_INSTANCE/ALiSS_agents/iHotfix $ZOPE_INSTANCE/Products/iHotfix && \  
ln -s $ZOPE_INSTANCE/ALiSS_agents/Five $ZOPE_INSTANCE/Products/Five && \  
ln -s $ZOPE_INSTANCE/ALiSS_agents/Epoz $ZOPE_INSTANCE/Products/Epoz && \  
ln -s $ZOPE_INSTANCE/ALiSS_agents/Epoz $ZOPE_INSTANCE/Products/Epoz && \  
ln -s $ZOPE_INSTANCE/ALiSS_agents/Extensions
$ZOPE_INSTANCE/Products/Extensions  
  
RUN mkdir -p $ZOPE_INSTANCE/var/ALiSS && cp
$ZOPE_INSTANCE/Products/ALiSS/data/aliss_stopwords.xliff
$ZOPE_INSTANCE/var/ALiSS  
  
USER root  
  
# Python 3.4 install  
RUN yum -y install epel-release && \  
yum install python34-devel -y && \  
curl -s "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \  
python3 get-pip.py && \  
  
# Chaperone install  
pip3 install chaperone && \  
yum clean all && rm -rf /tmp/*  
  
# Chaperone setup  
COPY chaperone.conf /etc/chaperone.d/chaperone.conf  
USER zope  
  
ENTRYPOINT ["/usr/bin/chaperone"]  
CMD ["--user", "zope"]  

