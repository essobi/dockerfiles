FROM ligo/lalsuite-dev:el7  
  
USER root  
  
# set up additional repositories  
RUN yum -y install curl  
RUN curl -L http://download.pegasus.isi.edu/wms/download/rhel/7/pegasus.repo >
/etc/yum.repos.d/pegasus.repo  
RUN curl -L http://htcondor.org/yum/RPM-GPG-KEY-HTCondor > RPM-GPG-KEY-
HTCondor  
RUN rpm --import RPM-GPG-KEY-HTCondor  
RUN rm -f RPM-GPG-KEY-HTCondor  
RUN curl -L http://htcondor.org/yum/repo.d/htcondor-stable-rhel7.repo >
/etc/yum.repos.d/htcondor-stable-rhel7.repo  
  
# clean up yum and update installed packages  
RUN yum clean all  
RUN yum makecache  
RUN yum -y update  
  
# install pycbc docker container software  
RUN yum -y install python2-pip python-setuptools  
RUN yum -y install git2u-all lscsoft-external-cbc  
RUN yum -y install zlib-devel libpng-devel libjpeg-devel libsqlite3-dev
sqlite-devel db4-devel openssl-devel  
RUN yum -y install hdf5-static libxml2-static zlib-static libstdc++-static
cfitsio-static glibc-static fftw-static gsl-static openssl-static  
RUN yum -y install tkinter libpng-devel lynx telnet wget  
RUN yum -y install compat-glibc compat-glibc-headers  
RUN yum -y install gd-devel audit-libs-devel libcap-devel nss-devel  
RUN yum -y install xmlto asciidoc hmaccalc newt-devel 'perl(ExtUtils::Embed)'
pesign elfutils-devel binutils-devel numactl-devel pciutils-devel  
RUN yum -y install dejagnu sharutils gcc-gnat libgnat dblatex gmp-devel mpfr-
devel libmpc-devel  
RUN yum -y install libuuid-devel netpbm-progs nasm  
RUN yum -y install gettext-devel avahi-devel dyninst-devel crash-devel
latex2html emacs libvirt-devel  
RUN yum -y install xmlto-tex patch  
RUN yum -y install ant asciidoc xsltproc fop docbook-style-xsl.noarch  
RUN yum -y install vim-enhanced man-db  
RUN yum -y install globus-gsi-cert-utils-progs gsi-openssh-clients osg-ca-
certs ligo-proxy-utils ecp-cookie-init  
RUN yum -y install condor condor-classads condor-python condor-procd condor-
external-libs  
RUN yum -y install pegasus  
RUN yum -y install lscsoft-all  
  
# set up sshd inside the docker container  
RUN yum -y install openssh-server  
EXPOSE 22  
ADD pycbc-sshd /usr/bin/pycbc-sshd  
RUN chmod +x /usr/bin/pycbc-sshd  
RUN mkdir -p /var/run/sshd  
  
# remove the LDG lal installation  
RUN yum -y remove "*lal*"  
  
# create a regular user account and switch to it  
RUN groupadd -g 1000 pycbc  
RUN useradd -u 1000 -g 1000 -ms /bin/bash pycbc  
USER pycbc  
WORKDIR /home/pycbc  
RUN cp -R /etc/skel/.??* ~  
  
RUN pip install virtualenv  
RUN virtualenv pycbc-software ; \  
source ~/pycbc-software/bin/activate ; \  
pip install --upgrade pip ; \  
pip install six packaging appdirs ; \  
pip install --upgrade setuptools ; \  
pip install "numpy>=1.6.4" "h5py>=2.5" unittest2 python-cjson Cython decorator
; \  
pip install "scipy>=0.13.0" ; \  
SWIG_FEATURES="-cpperraswarn -includeall -I/usr/include/openssl" pip install
M2Crypto ; \  
deactivate  
  
RUN source ~/pycbc-software/bin/activate ; \  
mkdir -p ~/src ; \  
cd ~/src ; \  
git clone https://github.com/lscsoft/lalsuite.git ; \  
cd ~/src/lalsuite ; \  
git checkout 95ad957cee1a37b7fc3128883d8b723556f9ec38 ; \  
./00boot ; \  
./configure --prefix=${VIRTUAL_ENV}/opt/lalsuite --enable-swig-python \  
\--disable-lalstochastic --disable-lalxml --disable-lalinference \  
\--disable-laldetchar --disable-lalapps 2>&1 | grep -v checking ; \  
make install ; \  
echo 'source ${VIRTUAL_ENV}/opt/lalsuite/etc/lalsuite-user-env.sh' >>
${VIRTUAL_ENV}/bin/activate ; \  
deactivate  
  
RUN source ~/pycbc-software/bin/activate ; \  
cd ~/src/lalsuite/lalapps ; \  
LIBS="-lhdf5_hl -lhdf5 -lcrypto -lssl -ldl -lz -lstdc++" ./configure
--prefix=${VIRTUAL_ENV}/opt/lalsuite \  
\--enable-static-binaries --disable-lalinference \  
\--disable-lalburst --disable-lalpulsar \  
\--disable-lalstochastic ; \  
cd ~/src/lalsuite/lalapps/src/lalapps ; \  
make ; \  
cd ~/src/lalsuite/lalapps/src/inspiral ;\  
make lalapps_inspinj ; \  
cp lalapps_inspinj $VIRTUAL_ENV/bin ; \  
deactivate  
  
RUN source ~/pycbc-software/bin/activate ; \  
pip install http://download.pegasus.isi.edu/pegasus/4.7.4/pegasus-python-
source-4.7.4.tar.gz ; \  
pip install dqsegdb ; \  
pip install "Sphinx>=1.4.2" numpydoc sphinx-rtd-theme ; \  
pip install "git+https://github.com/ligo-cbc/sphinxcontrib-
programoutput.git#egg=sphinxcontrib-programoutput" ; \  
pip install ipython jupyter hide_code; \  
jupyter nbextension install --sys-prefix --py hide_code; \  
jupyter nbextension enable \--sys-prefix --py hide_code; \  
jupyter serverextension enable \--sys-prefix --py hide_code; \  
deactivate  
  
RUN echo 'source ${HOME}/pycbc-software/bin/activate' >> ~/.bash_profile  

