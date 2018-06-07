FROM buildpack-deps:wheezy  
  
# remove several traces of debian python  
RUN apt-get purge -y python.*  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# gpg: key F73C700D: public key "Larry Hastings <larry@hastings.org>" imported  
ENV GPG_KEY 97FC712E4C024BBEA48A61ED3A5CA953F73C700D  
  
ENV PYTHON_VERSION 3.4.4  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 8.1.2  
RUN set -ex \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& ./configure --enable-shared --enable-unicode=ucs4 \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& pip3 install --no-cache-dir --upgrade --ignore-installed
pip==$PYTHON_PIP_VERSION \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python ~/.cache  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s easy_install-3.4 easy_install \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
RUN apt-get update  
RUN apt-get -y --force-yes install libmysqlclient-dev python3-pyqt4-dbg
python3-pyqt4.qtopengl-dbg python3-pyqt4.phonon-dbg libevent-dev
python3-setuptools libportaudio0 libportaudio2 libportaudiocpp0
portaudio19-dev python3-pip flac git apache2 php5 mysql-client mysql-server
tomcat6 vsftpd libapache2-mod-auth-mysql php5-mysql gcc-4.7 g++-4.7 mpg123 git
libtool build-essential pkg-config autoconf libdvbpsi-dev libasound2-dev
libxml2-dev libxpm-dev libsdl1.2-dev sdl-image1.2 libxcb-keysyms1-dev
libxinerama-dev libxext-dev qt4-dev-tools qtcreator  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 2578B775  
RUN git clone http://people.csail.mit.edu/hubert/git/pyaudio.git  
RUN cd pyaudio \ python3 setup.py install \ cd ..  
RUN pip3 install git+git://github.com/davispuh/MySQL-for-Python-3  
ADD . /SpeechRecognition-1.1.4  
RUN cd SpeechRecognition-1.1.4 \ python3 setup.py install \ cd ..  
ADD . /gTTS-master  
RUN cd gTTS-master \ python3 setup.py install \ cd ..  
ADD . /pygmaps-0.1.1  
RUN cd pygmaps-0.1.1 \ python3 setup.py install \ cd ..  
ADD . /pygeocoder-1.2.5  
RUN cd pygeocoder-1.2.5 \ python3 setup.py install \ cd ..  
ADD . /python-gmaps-0.2.1  
RUN cd python-gmaps-0.2.1 \ python3 setup.py install \ cd ..  
ADD . /pygeocoder  
RUN cd pygeocoder \ cp -n pygeolib.py /usr/local/lib/python3.4/dist-
packages/pygeocoder-1.2.5-py3.4.egg/pygeolib.py \ cp -n pygeocoder.py
/usr/local/lib/python3.4/dist-
packages/pygeocoder-1.2.5-py3.4.egg/pygeocoder.py \ cd ..  
ADD . /speech_recognition  
RUN cd speech_recognition \ cp -n __init__.py /usr/local/lib/python3.4/dist-
packages/speech_recognition \ cd ..  
ADD . /Bin  
  
CMD ["python3","main.py"]  

