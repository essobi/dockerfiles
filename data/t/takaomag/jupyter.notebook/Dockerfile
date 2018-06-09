# jupyter.notebook  
  
FROM takaomag/spark:release-2.2.1-2017.12.18.09.45  
  
ENV \  
X_DOCKER_REPO_NAME=jupyter.notebook \  
# X_XGBOOST_VERSION=0.6 \  
X_XGBOOST_GIT_CHECKOUT=master \  
X_LIBRDKAFKA_GIT_CHECKOUT=master \  
# X_LIBRDKAFKA_VERSION=0.11.0 \  
X_MYSQL_CONNECTOR_C_VERSOIN=6.1.11 \  
X_MYSQL_CONNECTOR_PYTHON_VERSION=8.0.5  
  
  
COPY \  
mysql-connector-c-6.1.11-src.tar.gz /var/tmp/  
  
RUN \  
echo "2016-04-22-0" > /dev/null && \  
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
# https://docs.continuum.io/anaconda/packages/pkg-docs  
# Because cairo-infinality-ultimate and cairo are in conflict, install
infinality-bundle in advance.  
# grep --silent 'infinality-bundle' /etc/pacman.conf || (echo -e "#
${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} >>>\n[infinality-bundle]\nServer =
http://bohoomil.com/repo/\$arch\n# ${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} <<<\n"
>> /etc/pacman.conf && pacman-key -r 962DDE58 && pacman-key --lsign-key
962DDE58 && sudo -u nobody yaourt -Syy) && \  
# REQUIRED_PACKAGES=("libsm" "pandoc" "texlive-most" "texlive-langcjk"
"libxrender" "llvm" "hdf5-cpp-fortran" "ttf-dejavu" "otf-ipafont" "ttf-mplus"
"npm" "nodejs") && \  
# REQUIRED_PACKAGES=("infinality-bundle" "libsm" "pandoc" "texlive-most"
"texlive-langcjk" "libxrender" "llvm" "hdf5-cpp-fortran" "ttf-dejavu" "otf-
ipafont" "ttf-mplus" "npm" "nodejs" "protobuf" "blosc" "libev" "lz4" "snappy")
&& \  
# REQUIRED_PACKAGES=("libsm" "pandoc" "texlive-most" "texlive-langcjk"
"libxrender" "llvm" "hdf5-cpp-fortran" "ttf-dejavu" "otf-ipafont" "ttf-mplus"
"npm" "nodejs" "protobuf" "protobuf-c" "blosc" "libev" "lz4" "lzo" "snappy"
"zstd" "brotli") && \  
: && \  
# arrow and parquet-cpp are excluded because of make dependency  
REQUIRED_PACKAGES=("apr" "autoconf" "automake" "boost" "boost-libs" "blosc"
"brotli" "bzip2" "ccache" "cmake" "expat" "flatbuffers" "gcc-fortran"
"jemalloc" "hdf5" "rapidjson" "thrift" "libev" "libevent" "libffi"
"libmariadbclient" "libsm" "libsodium" "llvm" "m4" "ncurses" "nodejs" "npm"
"pango" "pandoc" "pcre" "postgresql-libs" "protobuf" "protobuf-c" "readline"
"texlive-most" "texlive-langjapanese" "libxrender" "ttf-dejavu" "otf-ipafont"
"ttf-mplus" "lz4" "lzo" "snappy" "xz" "zeromq" "zlib" "zstd") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm "${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
: && \  
REQUIRED_PYTHON_MODULES_0=("Cython" "cffi" "gevent" "lz4" "lz4tools" "python-
lzo" "python-snappy" "zstd" "Brotli" "brotlipy" "flatbuffers" "python-
rapidjson" "scales" "param") && \  
# removed aiogremlin, aredis  
REQUIRED_PYTHON_MODULES_1=("affine" "appdirs" "attrs" "automat" "apptools"
"bcolz" "bcrypt" "bitarray" "holoviews[all]" "Blaze" "Bleach" "blist" "Bokeh"
"boto3" "botocore" "Bottlechest" "Bottleneck" "bz2file" "cachecontrol"
"cached-property" "chardet" "chest" "click" "click-plugins" "cligj"
"cloudpickle" "colander" "colorama" "configobj" "contextlib2" "cookies"
"cornice" "cryptography" "csvkit" "cubes" "cymem" "cytoolz" "dask[complete]"
"dill" "DataShape" "distributed" "dnspython" "ecdsa" "envisage" "fastcache"
"filelock" "genson" "gitdb2" "gitpython" "h5py" "humanize" "idna"
"incremental" "ipywidgets" "iso8601" "itsdangerous" "jinja2" "jmespath"
"joblib" "jsonschema" "jupyter" "jupyterhub" "lazy-object-proxy" "locket"
"lockfile" "luigi" "matplotlib" "mock" "more-itertools" "msgpack-python"
"multipledispatch" "munch" "neon" "networkx" "nltk" "notebook" "numexpr" "odo"
"orange3" "pandas" "pandas-datareader" "japandas" "pandasql" "partd" "passlib"
"patsy" "petl" "pexpect" "picklable-itertools" "plotly" "progressbar2"
"prompt_toolkit" "pgcli" "mycli" "wharfee" "saws" "aws-shell" "http-prompt"
"protobuf" "psutil" "psycopg2" "pycodestyle" "pydocstyle" "pycrypto" "pycurl"
"tables" "python-dateutil" "pytz" "pyzmq" "qgrid" "quandl" "queuelib"
"requests" "requests-file" "responses" "rope" "s3fs" "scikit-learn" "seaborn"
"semantic_version" "semver" "simplegeneric" "simplejson" "smart_open"
"sortedcollections" "sortedcontainers" "spacy" "sqlalchemy" "sqlparse"
"statsmodels" "sympy" "tblib" "terminado" "testpath" "tqdm" "traitlets"
"traits" "transaction" "ujson" "unicodecsv" "venusian" "wrapt" "zict"
"chainer" "cymysql" "oursql3" "mysqlclient" "prettyplotlib" "PyHive"
"holidays-jp" "cassandra-driver" "hyperopt" "airflow[async, devel,
devel_hadoop, celery, crypto, druid, jdbc, hdfs, mysql, password, postgres,
s3, slack]" "python-memcached" "libmc" "redis" "gremlinpython" "docker"
"fastparquet" "pyarrow" "feather-format" "pyproj" "systemd-python" "lightgbm")
&& \  
echo -e "${FONT_INFO}[INFO] Install required python packages
[${REQUIRED_PYTHON_MODULES_0[@]}]${FONT_DEFAULT}" && \  
/opt/local/python-3/bin/pip3 install --upgrade
"${REQUIRED_PYTHON_MODULES_0[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PYTHON_MODULES_0[@]}]${FONT_DEFAULT}" && \  
## Because numba setup.py requires Cython, install it after Cython has been
installed.  
: && \  
# echo -e "${FONT_INFO}[INFO] Install python llvmlite${FONT_DEFAULT}" && \  
# cd /var/tmp && \  
# /opt/local/python-3/bin/pip3 download --no-deps --no-binary :all: llvmlite
&& \  
# _fname=$(ls -A | grep llvmlite) && \  
# ([[ "${_fname: -3:3}" = 'zip' ]] && unzip -q ${_fname} || tar xzf ${_fname})
&& \  
# rm -f ${_fname} && \  
# _dname=$(ls -A | grep llvmlite) && \  
# X_LLVMLITE_VERSION=$(egrep -e '^llvmlite-.+$' <<< ${_dname} | head -1 | cut
-d '-' -f 2) && \  
# cd ${_dname} && \  
# /opt/local/python-3/bin/python3 setup.py build && \  
# /opt/local/python-3/bin/python3 setup.py install && \  
# cd .. && \  
# rm -rf ${_dname} && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install python llvmlite${FONT_DEFAULT}" &&
\  
: && \  
# echo -e "${FONT_INFO}[INFO] Install python numba${FONT_DEFAULT}" && \  
# cd /var/tmp && \  
# /opt/local/python-3/bin/pip3 download --no-deps --no-binary :all: numba && \  
# _fname=$(ls -A | grep numba) && \  
# ([[ "${_fname: -3:3}" = 'zip' ]] && unzip -q ${_fname} || tar xzf ${_fname})
&& \  
# rm -f ${_fname} && \  
# _dname=$(ls -A | grep numba) && \  
# X_NUMBA_VERSION=$(egrep -e '^numba-.+$' <<< ${_dname} | head -1 | cut -d '-'
-f 2) && \  
# cd ${_dname} && \  
# /opt/local/python-3/bin/python3 setup.py build_ext --inplace && \  
# /opt/local/python-3/bin/python3 setup.py install && \  
# cd .. && \  
# rm -rf ${_dname} && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install python numba${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required python packages
[${REQUIRED_PYTHON_MODULES_1[@]}]${FONT_DEFAULT}" && \  
/opt/local/python-3/bin/pip3 install --upgrade
"${REQUIRED_PYTHON_MODULES_1[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PYTHON_MODULES_1[@]}]${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install mysql-connector-c
${X_MYSQL_CONNECTOR_C_VERSOIN}{FONT_DEFAULT}" && \  
cd /var/tmp && \  
tar xvzf mysql-connector-c-${X_MYSQL_CONNECTOR_C_VERSOIN}-src.tar.gz && \  
cd mysql-connector-c-${X_MYSQL_CONNECTOR_C_VERSOIN}-src && \  
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/opt/local/mysql-
connector-c-${X_MYSQL_CONNECTOR_C_VERSOIN} && \  
porg --log \--package="mysql-connector-c-${X_MYSQL_CONNECTOR_C_VERSOIN}" \--
make install && \  
porg --log \--package="mysql-connector-c-${X_MYSQL_CONNECTOR_C_VERSOIN}" -+ --
ln -sf /opt/local/mysql-connector-c-${X_MYSQL_CONNECTOR_C_VERSOIN}
/opt/local/mysql-connector-c && \  
cd /var/tmp && \  
rm -rf mysql-connector-c-* && \  
echo -e "${FONT_SUCCESS}[INFO] Install mysql-connector-c
${X_MYSQL_CONNECTOR_C_VERSOIN}{FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install mysql-connector-python
${X_MYSQL_CONNECTOR_PYTHON_VERSOIN}{FONT_DEFAULT}" && \  
cd /var/tmp && \  
curl --silent --location --fail --retry 5 "https://github.com/mysql/mysql-
connector-python/archive/${X_MYSQL_CONNECTOR_PYTHON_VERSION}.tar.gz" | tar xz
&& \  
cd mysql-connector-python-${X_MYSQL_CONNECTOR_PYTHON_VERSION}/ && \  
# export MYSQLXPB_PROTOBUF_LIB_DIR=/usr/lib && \  
# export MYSQLXPB_PROTOC=/usr/bin/protoc && \  
# export MYSQLXPB_PROTOBUF_INCLUDE_DIR=/usr/include && \  
/opt/local/python-3/bin/python3 setup.py install --with-mysql-
capi=/opt/local/mysql-connector-c-${X_MYSQL_CONNECTOR_C_VERSOIN} \--with-
protobuf-include-dir=/usr/include --with-protobuf-lib-dir=/usr/lib --with-
protoc=/usr/bin/protoc --static && \  
cd /var/tmp && \  
rm -rf mysql-connector-python-* && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install mysql-connector-python
${X_MYSQL_CONNECTOR_PYTHON_VERSOIN}{FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install xgboost${FONT_DEFAULT}" && \  
cd /var/tmp && \  
if [[ "${X_XGBOOST_VERSION}" ]];then\  
curl --fail --silent --location --retry 5
"https://github.com/dmlc/xgboost/archive/v${X_XGBOOST_VERSION}.tar.gz" | tar
xz; \  
elif [[ "${X_XGBOOST_GIT_CHECKOUT}" ]];then\  
git clone -b ${X_XGBOOST_GIT_CHECKOUT} \--recursive
https://github.com/dmlc/xgboost.git && \  
mv xgboost xgboost-${X_XGBOOST_GIT_CHECKOUT} && \  
export X_XGBOOST_VERSION=${X_XGBOOST_GIT_CHECKOUT}; \  
else\  
echo -e "${FONT_ERROR}[ERROR] Both X_XGBOOST_VERSION and
X_XGBOOST_GIT_CHECKOUT is specified.${FONT_DEFAULT}" 1>&2 && \  
exit 1; \  
fi && \  
cd xgboost-${X_XGBOOST_VERSION} && \  
make -j $(nproc) && \  
mkdir /opt/local/xgboost-${X_XGBOOST_VERSION} && \  
porg --log \--package="xgboost-${X_XGBOOST_VERSION}" \-- mv ./lib
/opt/local/xgboost-${X_XGBOOST_VERSION}/. && \  
porg --log \--package="xgboost-${X_XGBOOST_VERSION}" -+ -- ln -sf
/opt/local/xgboost-${X_XGBOOST_VERSION}/lib $(/opt/local/python-3/bin/python3
-c 'import os, sys;print(os.path.join(sys.prefix, "xgboost"))') && \  
cd python-package && \  
/opt/local/python-3/bin/python3 setup.py install && \  
cd /var/tmp && \  
rm -rf xgboost-${X_XGBOOST_VERSION} && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install xgboost${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install
librdkafka-${X_LIBRDKAFKA_VERSION}${X_LIBRDKAFKA_GIT_CHECKOUT}${FONT_DEFAULT}"
&& \  
cd /var/tmp && \  
if [[ "${X_LIBRDKAFKA_VERSION}" ]];then\  
curl --silent --location --fail --retry 5
"https://github.com/edenhill/librdkafka/archive/v${X_LIBRDKAFKA_VERSION}.tar.gz"
| tar xz; \  
elif [[ "${X_LIBRDKAFKA_GIT_CHECKOUT}" ]];then\  
git clone -b ${X_LIBRDKAFKA_GIT_CHECKOUT}
https://github.com/edenhill/librdkafka && \  
cd librdkafka && \  
# git checkout ${X_LIBRDKAFKA_GIT_CHECKOUT} && \  
export X_LIBRDKAFKA_VERSION=${X_LIBRDKAFKA_GIT_CHECKOUT} && \  
cd ../ && \  
mv librdkafka librdkafka-${X_LIBRDKAFKA_VERSION}; \  
else\  
echo -e "${FONT_ERROR}[ERROR] Either X_LIBRDKAFKA_VERSION or
X_LIBRDKAFKA_GIT_CHECKOUT must be specified.${FONT_DEFAULT}" 1>&2; \  
exit 1; \  
fi && \  
cd librdkafka-${X_LIBRDKAFKA_VERSION} && \  
./configure --prefix /opt/local/librdkafka-${X_LIBRDKAFKA_VERSION} && \  
make -j $(( $(nproc) + 2 )) && \  
porg --log \--package=librdkafka-${X_LIBRDKAFKA_VERSION} \-- make install && \  
cd ../ && \  
rm -rf librdkafka-${X_LIBRDKAFKA_VERSION} && \  
echo "/opt/local/librdkafka-${X_LIBRDKAFKA_VERSION}/lib" >
librdkafka-${X_LIBRDKAFKA_VERSION}.conf && \  
porg --log \--package=librdkafka-${X_LIBRDKAFKA_VERSION} -+ -- mv
librdkafka-${X_LIBRDKAFKA_VERSION}.conf /etc/ld.so.conf.d/. && \  
ldconfig && \  
cd /opt/local && \  
porg --log \--package=librdkafka-${X_LIBRDKAFKA_VERSION} -+ -- ln -s
librdkafka-${X_LIBRDKAFKA_VERSION} librdkafka && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install librdkafka${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required python packages [kafka-python
confluent-kafka]${FONT_DEFAULT}" && \  
/opt/local/python-3/bin/pip3 install --upgrade lz4 lz4tools xxhash python-
snappy && \  
/opt/local/python-3/bin/pip3 install --upgrade kafka-python && \  
/opt/local/python-3/bin/pip3 install --upgrade --global-option=build_ext
--global-option="-I/opt/local/librdkafka-${X_LIBRDKAFKA_VERSION}/include"
\--global-option="-L/opt/local/librdkafka-${X_LIBRDKAFKA_VERSION}/lib"
confluent-kafka && \  
/opt/local/python-3/bin/pip3 install --upgrade --global-option=build_ext
--global-option="-I/opt/local/librdkafka-${X_LIBRDKAFKA_VERSION}/include"
\--global-option="-L/opt/local/librdkafka-${X_LIBRDKAFKA_VERSION}/lib"
confluent-kafka[avro] && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages [kafka-python
confluent-kafka]${FONT_DEFAULT}" && \  
: && \  
cd /var/tmp && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
rm -f /etc/machine-id  
  
EXPOSE \  
8888  
  
# spark.mesos.executor.docker.image assumes the default working directory of
the container to be inside $SPARK_HOME.  
# WORKDIR /opt/local/spark (inherit from takaomag/spark)  
# WORKDIR /opt/work/jupyter.notebook  
  
ENTRYPOINT ["/opt/local/python-3/bin/jupyter"]  
CMD ["notebook", "--ip=::1", "--no-browser"]  

