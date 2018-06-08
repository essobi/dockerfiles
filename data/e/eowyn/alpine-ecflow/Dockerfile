FROM alpine  
RUN apk update \  
&& apk add --no-cache build-base cmake g++ linux-headers openssl python3-dev
ca-certificates wget vim \  
&& update-ca-certificates  
ENV ECFLOW_VERSION=4.9.0  
ENV BOOST_VERSION=1.53.0  
ENV DBUILD=/tmp/ecflow_build  
RUN mkdir ${DBUILD}  
  
RUN cd ${DBUILD} \  
&& export BOOST_TGZ=boost_$(echo ${BOOST_VERSION} | tr '.' '_').tar.gz \  
ETGZ=ecFlow.tgz \  
HTTPB=https://sourceforge.net/projects/boost/files/boost \  
HTTPE=https://software.ecmwf.int/wiki/download/attachments/8650755 \  
&& wget -O ${ETGZ} ${HTTPE}/ecFlow-$ECFLOW_VERSION-Source.tar.gz?api=v2 \  
&& wget -O ${BOOST_TGZ} ${HTTPE}/${BOOST_TGZ}?api=v2 \  
&& tar -xzf ${ETGZ} \  
&& tar -xzf ${BOOST_TGZ} \  
&& rm ${BOOST_TGZ} ${ETGZ}  
  
RUN cd ${DBUILD} \  
&& export WK=${DBUILD}/ecFlow-${ECFLOW_VERSION}-Source \  
BOOST_ROOT=${DBUILD}/boost_$(echo ${BOOST_VERSION} | tr '.' '_') \  
&& cd ${BOOST_ROOT} \  
&& python_root=$(python3 -c "import sys; print(sys.prefix)") \  
&& ./bootstrap.sh --with-python-root=$python_root \  
\--with-python=/usr/bin/python3 \  
&& sed -i "s|using python : 3.6 : ;|using python : 3 : python3 :
/usr/include/python ;|g" project-config.jam \  
&& ln -sf /usr/include/python3.6m /usr/include/python \  
&& ln -sf /usr/include/python3.6m /usr/include/python3.6 \  
&& $WK/build_scripts/boost_1_53_fix.sh \  
&& $WK/build_scripts/boost_build.sh \  
&& mkdir -p $WK/build  
  
RUN export WK=${DBUILD}/ecFlow-${ECFLOW_VERSION}-Source \  
BOOST_ROOT=${DBUILD}/boost_$(echo ${BOOST_VERSION} | tr '.' '_') \  
&& cd $WK/build \  
&& sed -i '1s/^/cmake_policy(SET CMP0004 OLD)/'
../cmake/ecbuild_add_library.cmake \  
&& cmake -DCMAKE_CXX_FLAGS=-w -DENABLE_GUI=OFF -DENABLE_UI=OFF .. \  
&& make -j$(grep processor /proc/cpuinfo | wc -l) \  
&& make install  
  
RUN apk del cmake g++ linux-headers build-base  
RUN rm -rf ${DBUILD}  
  
RUN adduser -SD ecflow  
WORKDIR /home/ecflow  
USER ecflow  
EXPOSE 2500  
ENTRYPOINT ["/usr/local/bin/ecflow_server", "-d", "-p 2500"]  
ENV ECFLOW_USER=ecflow \  
ECF_PORT=2500 \  
ECF_HOME=/home/ecflow \  
HOME=/home/ecflow \  
HOST=ecflow \  
LANG=en_US.UTF-8 \  
PYTHONPATH=/usr/local/lib/python3/site-packages  
  
# https://pkgs.alpinelinux.org/packages?name=build-
base&branch=&repo=&arch=&maintainer=  

