#  
# Python versions and specific gpsd version  
# for testing python-gpsdshm.  
#  
# Markus Juenemann, 04-Feb-2016  
FROM mjuenema/pythons:latest  
MAINTAINER Markus Juenemann <markus@juenemann.net>  
USER root  
  
# Yum proxy  
#  
RUN [ "$http_proxy" == "" ] || echo "proxy=$http_proxy" >> /etc/yum.conf  
RUN yum clean all  
  
RUN yum -y install python-devel chrpath automake pcre-devel \  
bison byacc gcc-c++ libxslt xmlto  
  
RUN pip2.7 install --egg SCons  
  
RUN git clone http://git.savannah.gnu.org/r/gpsd.git  
  
# gpsd-3.16 is used for gpsfake  
RUN cd ~/gpsd && \  
git checkout release-3.16 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shared=yes shm_export=yes python=yes
leapfetch=no prefix=/opt/gpsd/3.16 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.15 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shared=yes shm_export=yes python=yes
leapfetch=no prefix=/opt/gpsd/3.15 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.14 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shared=yes shm_export=yes python=yes
leapfetch=no prefix=/opt/gpsd/3.14 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.13 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shared=yes shm_export=yes python=yes
leapfetch=no prefix=/opt/gpsd/3.13 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.12 && \  
git clean -f && \  
python2.7 /usr/local/bin/scons minimal=yes shared=yes netfeed=yes
shm_export=yes python=no leapfetch=yes prefix=/opt/gpsd/3.12 install && \  
cp -v *.h /opt/gpsd/3.12/include && \  
mkdir -vp /opt/gpsd/3.12/python && \  
cp -v gps/* /opt/gpsd/3.12/python  
  
RUN cd ~/gpsd && \  
git checkout release-3.11 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.11 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.10 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.10 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.9 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.9 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.8 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.8 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.7 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.7 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.6 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.6 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.5 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.5 && \  
python2.7 /usr/local/bin/scons install  
  
# gpsd 3.4 needs some work-arounds leapseconds.cache file.  
RUN cd ~/gpsd && \  
git checkout release-3.4 && \  
git clean -f && rm -fv leapseconds.cache && \  
python2.7 /usr/local/bin/scons shared=yes minimal=yes netfeed=yes
shm_export=yes python=no leapfetch=yes prefix=/opt/gpsd/3.4 install && \  
git checkout -- leapseconds.cache  
  
RUN cd ~/gpsd && \  
git checkout release-3.3 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.3 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.2 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.2 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.1 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.1 && \  
python2.7 /usr/local/bin/scons install  
  
RUN cd ~/gpsd && \  
git checkout release-3.0 && \  
python2.7 /usr/local/bin/scons -c && \  
python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no
prefix=/opt/gpsd/3.0 && \  
python2.7 /usr/local/bin/scons install  
  
# git checkout release-3.0 && \  
# git clean -f && \  
# python2.7 /usr/local/bin/scons shm_export=yes leapfetch=yes python=no
prefix=/opt/gpsd/3.0 install  
# python2.7 /usr/local/bin/scons -c && \  
# python2.7 /usr/local/bin/scons shm_export=yes python=no leapfetch=no
prefix=/opt/gpsd/3.0 && \  
# python2.7 /usr/local/bin/scons install  
#RUN cd ~ && \  
# git clone https://github.com/mjuenema/python-gpsdshm.git  
RUN cd ~ && \  
git clone https://github.com/swig/swig.git && \  
cd swig && \  
git checkout rel-3.0.8 && \  
sh autogen.sh && \  
./configure && \  
make && \  
make install  
  
RUN mkdir -vp /home/developer/.cache/pip /home/developer/.ccache
/home/developer/src  
  
CMD /bin/bash  
  
RUN yum -y install ccache && \  
ln -s `which ccache` /usr/local/bin/gcc && \  
ln -s `which ccache` /usr/local/bin/g++ && \  
ln -s `which ccache` /usr/local/bin/cc && \  
ln -s `which ccache` /usr/local/bin/c++  
  
#RUN cd ~ && \  
# wget https://pypi.python.org/packages/source/S/SCons/scons-2.4.1.tar.gz && \  
# tar xvfz scons-2.4.1.tar.gz && \  
# cd scons-2.4.1 && \  
# python2.7 setup.py install  
# Undo yum proxy  
#  
RUN [ "$http_proxy" == "" ] || sed --in-place 's/^proxy=http.*$//g'
/etc/yum.conf  
  
COPY tests.run /run_tests.sh  

