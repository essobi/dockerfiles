# openblas  
# OpenBLAS and multi-thread problem on Docker automated-build  
# http://e-kwsm.hatenablog.com/entry/2015/03/04/221810  
# http://stackoverflow.com/questions/27919866/docker-images-with-architecture-
optimisation  
# https://www.archlinux.org/packages/extra/x86_64/blas/  
# https://aur.archlinux.org/packages/openblas-lapack/  
# https://aur.archlinux.org/packages/intel-mkl/  
# http://qiita.com/yukiB/items/bec24db4a5a41db02895  
# http://qiita.com/_akisato/items/d5de60e38b5a69387bde  
# http://qiita.com/unnonouno/items/8ab453a1868d77a93679  
# https://github.com/numpy/numpy/blob/master/site.cfg.example  
# http://stackoverflow.com/questions/13769936/supplying-numpy-site-cfg-
arguments-to-pip/13796808#13796808  
# https://brucebcampbell.wordpress.com/2014/12/04/setting-up-native-atlas-
with-netlib-java/  
# https://github.com/fommil/netlib-java  
# https://github.com/xianyi/OpenBLAS/issues/735  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=openblas \  
X_OPENBLAS_VERSION=0.2.20 \  
# X_OPENBLAS_GIT_CHECKOUT=master \  
X_LAPACK_VERSION=3.7.0  
RUN \  
echo "2016-05-06-1" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
: && \  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
: && \  
# echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}"
&& \  
# pacman-key --refresh-keys && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
: && \  
# REQUIRED_PACKAGES=("gcc-fortran" "atlas-lapack-base") && \  
# REQUIRED_PACKAGES=("gcc-fortran" "atlas-lapack") && \  
REQUIRED_PACKAGES=("gcc-fortran") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install
OpenBLAS-${X_OPENBLAS_VERSION}${FONT_DEFAULT}" && \  
export X_CPU_COUNT=32 && \  
cd /var/tmp && \  
if [[ "${X_OPENBLAS_VERSION}" ]];then\  
curl --fail --silent --location --retry 5
"https://github.com/xianyi/OpenBLAS/archive/v${X_OPENBLAS_VERSION}.tar.gz" |
tar xz; \  
elif [[ "${X_OPENBLAS_GIT_CHECKOUT}" ]];then\  
git clone -q -b ${X_OPENBLAS_GIT_CHECKOUT}
https://github.com/xianyi/OpenBLAS.git && \  
mv OpenBLAS OpenBLAS-${X_OPENBLAS_GIT_CHECKOUT} && \  
export X_OPENBLAS_VERSION=${X_OPENBLAS_GIT_CHECKOUT}; \  
else\  
echo -e "${FONT_ERROR}[ERROR] Both X_OPENBLAS_VERSION and
X_OPENBLAS_GIT_CHECKOUT is specified.${FONT_DEFAULT}" 1>&2; \  
exit 1; \  
fi && \  
: && \  
cd OpenBLAS-${X_OPENBLAS_VERSION} && \  
# LIBPREFIX=libblas \  
# ARCH=x86_64 \  
# NO_AVX=0 \  
# NO_AVX2=0 \  
# NO_LAPACK=0 \  
# NO_LAPACKE=1 \  
# NO_CBLAS=0 \  
# NO_AFFINITY=1 \  
# INTERFACE64=1 \  
# OPENBLAS_MAKE_ARGS="FC=gfortran DYNAMIC_ARCH=1 BINARY=64 USE_OPENMP=0
MAJOR_VERSION=${X_LAPACK_VERSION:0:1} NO_LAPACK=0 BUILD_LAPACK_DEPRECATED=1
USE_THREAD=1 NUM_THREADS=${X_CPU_COUNT:-$(($(grep 'physical id'
/proc/cpuinfo|sort|uniq|wc -l) * $(grep 'cores' /proc/cpuinfo|sort|tail -n
1|sed -e 's/cpu cores.*: //')))}" && \  
OPENBLAS_MAKE_ARGS="FC=gfortran DYNAMIC_ARCH=1 BINARY=64 INTERFACE64=1
USE_OPENMP=0 MAJOR_VERSION=${X_LAPACK_VERSION:0:1} NO_LAPACK=0
BUILD_LAPACK_DEPRECATED=1 USE_THREAD=1 NUM_THREADS=${X_CPU_COUNT:-$(($(grep
'physical id' /proc/cpuinfo|sort|uniq|wc -l) * $(grep 'cores'
/proc/cpuinfo|sort|tail -n 1|sed -e 's/cpu cores.*: //')))}" && \  
make ${OPENBLAS_MAKE_ARGS} && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" \-- make PREFIX=/usr
${OPENBLAS_MAKE_ARGS} install && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- install -Dm644
LICENSE "/usr/share/licenses/OpenBLAS-${X_OPENBLAS_VERSION}/LICENSE" && \  
cd .. && \  
rm -rf OpenBLAS-${X_OPENBLAS_VERSION} && \  
cd /usr/lib && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- ln -sf
libopenblas.so libblas.so && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- ln -sf
libopenblas.so libblas.so.${X_LAPACK_VERSION:0:1} && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- ln -sf
libopenblas.so libblas.so.${X_LAPACK_VERSION} && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- ln -sf
libopenblas.so libcblas.so && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- ln -sf
libopenblas.so liblapack.so && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- ln -sf
libopenblas.so liblapack.so.${X_LAPACK_VERSION:0:1} && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- ln -sf
libopenblas.so liblapack.so.${X_LAPACK_VERSION} && \  
porg --log \--package="OpenBLAS-${X_OPENBLAS_VERSION}" -+ -- ln -sf
libopenblas.so liblapacke.so && \  
cd /opt/local && \  
# ln -sf /opt/local/OpenBLAS-${X_OPENBLAS_VERSION} /opt/local/OpenBLAS && \  
ldconfig && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
OpenBLAS-${X_OPENBLAS_VERSION}${FONT_DEFAULT}" && \  
: && \  
REQUIRED_PYTHON_MODULES=("Cython") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required python packages
[${REQUIRED_PYTHON_MODULES[@]}]${FONT_DEFAULT}" && \  
/opt/local/python-3/bin/pip3 install --upgrade "${REQUIRED_PYTHON_MODULES[@]}"
&& \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required python packages
[${REQUIRED_PYTHON_MODULES[@]}]${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install python numpy with OpenBLAS${FONT_DEFAULT}"
&& \  
# echo $'[ALL]\n\  
#library_dirs = /usr/local/lib\n\  
#include_dirs = /usr/local/include\n\  
#\n\  
#[openblas]\n\  
#libraries = openblas\n\  
#library_dirs = /usr/lib\n\  
#include_dirs = /usr/include\n\  
#runtime_library_dirs = /usr/lib\n\  
#' > /root/.numpy-site.cfg && \  
## echo $'\n[mkl]\n\  
##library_dirs = /opt/intel/mkl/lib/intel64\n\  
##include_dirs = /opt/intel/mkl/include\n\  
##mkl_libs = mkl_rt\n\  
##lapack_libs =\n\  
##' >> /root/.numpy-site.cfg;\  
# /opt/local/python-3/bin/pip3 install --upgrade --no-binary :all: numpy && \  
# /opt/local/python-3/bin/pip3 install --upgrade --no-binary :all: scipy && \  
cd /var/tmp && \  
/opt/local/python-3/bin/pip3 download --no-deps --no-binary :all: numpy && \  
_fname=$(ls -A | grep numpy) && \  
([[ "${_fname: -3:3}" = 'zip' ]] && unzip -q ${_fname} || tar xzf ${_fname})
&& \  
rm -f ${_fname} && \  
_dname=$(ls -A | grep numpy) && \  
X_NUMPY_VERSION=$(egrep -e '^numpy-.+$' <<< ${_dname} | head -1 | cut -d '-'
-f 2) && \  
cd ${_dname} && \  
echo $'[ALL]\n\  
library_dirs = /usr/lib\n\  
include_dirs = /usr/include\n\  
\n\  
[openblas]\n\  
libraries = openblas\n\  
library_dirs = /usr/lib\n\  
include_dirs = /usr/include\n\  
runtime_library_dirs = /usr/lib\n\  
' > site.cfg && \  
# export ATLAS=None && \  
export LDFLAGS="-shared" && \  
/opt/local/python-3/bin/python3 setup.py config_fc --fcompiler=gnu95 build &&
\  
/opt/local/python-3/bin/python3 setup.py config_fc --fcompiler=gnu95 install
--prefix=/opt/local/python-3 --optimize=1 && \  
([[ ! -d "/opt/local/python-3/lib/python${X_PY3_VERSION:0:3}/site-
packages/numpy-${X_NUMPY_VERSION}-py${X_PY3_VERSION:0:3}-linux-x86_64.egg/numpy/core/include/numpy"
]] || ln -sf /opt/local/python-3/lib/python${X_PY3_VERSION:0:3}/site-
packages/numpy-${X_NUMPY_VERSION}-py${X_PY3_VERSION:0:3}-linux-x86_64.egg/numpy/core/include/numpy
/opt/local/python-3/include/python${X_PY3_VERSION:0:3}m/numpy) && \  
unset ATLAS && \  
unset LDFLAGS && \  
cd .. && \  
rm -rf ${_dname} && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install python numpy with
OpenBLAS${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install python scipy with OpenBLAS${FONT_DEFAULT}"
&& \  
cd /var/tmp && \  
/opt/local/python-3/bin/pip3 download --no-deps --no-binary :all: scipy && \  
_fname=$(ls -A | grep scipy) && \  
([[ "${_fname: -3:3}" = 'zip' ]] && unzip -q ${_fname} || tar xzf ${_fname})
&& \  
rm -f ${_fname} && \  
_dname=$(ls -A | grep scipy) && \  
cd ${_dname} && \  
echo $'[ALL]\n\  
library_dirs = /usr/lib\n\  
include_dirs = /usr/include\n\  
\n\  
[openblas]\n\  
libraries = openblas\n\  
library_dirs = /usr/lib\n\  
include_dirs = /usr/include\n\  
runtime_library_dirs = /usr/lib\n\  
' > site.cfg && \  
# export ATLAS=None && \  
export LDFLAGS="-shared" && \  
/opt/local/python-3/bin/python3 setup.py config_fc --fcompiler=gnu95 build &&
\  
/opt/local/python-3/bin/python3 setup.py config_fc --fcompiler=gnu95 install
--prefix=/opt/local/python-3 --optimize=1 && \  
unset ATLAS && \  
unset LDFLAGS && \  
cd .. && \  
rm -rf ${_dname} && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install python scipy with
OpenBLAS${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
ENV \  
OPENBLAS_MAIN_FREE=1 \  
OPENBLAS_NUM_THREADS=1  

