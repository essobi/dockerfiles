FROM resin/rpi-raspbian:jessie
MAINTAINER Carlos Sánchez

ENV QEMU_EXECVE 1
COPY . /usr/bin
RUN [ "cross-build-start" ]

RUN  sed -i 's/jessie/stretch/g' /etc/apt/sources.list                      && \
     apt-get update                                                         && \
     apt-get install -y --no-install-recommends                                \
	 git                                                                   \
	 python2.7 \
	 python2.7-dev                                                         \
	 python-pip                                                            \
	 python-setuptools                                                     \
	 python-wheel                                                          \
	 python3.4 \
	 python3.4-dev                                                         \
	 python3.5 \
	 python3.5-dev                                                         \
	 pypy                                                                  \
	 pypy-dev                                                              \
	 libffi-dev                                                            \
	 libasound2-dev                                                        \
	 pandoc                                                                \
	 build-essential                                                    && \
	 pip install coveralls tox                                          && \
     apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD https://github.com/sashahilton00/spotify-connect-resources/raw/master/libs/armhf/armv7/release-esdk-1.20.0-v1.20.0-g594175d4/libspotify_embedded_shared.so /usr/lib/

ENTRYPOINT ["/bin/bash"]

RUN [ "cross-build-end" ]
