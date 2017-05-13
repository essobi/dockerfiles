FROM python:slim
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

ADD requirements.txt /tmp/requirements.txt

RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN apt-get update && apt-get install -y --no-install-recommends \
		build-essential \
		ca-certificates \
		git \
		ssh \
		libexpat1 \
		libmysqlclient18 \
		libmysqlclient-dev \
		python3-dev \
		wget \
# grab gosu for easy step-down from root
&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
&& gpg --verify /usr/local/bin/gosu.asc \
&& rm /usr/local/bin/gosu.asc \
&& chmod +x /usr/local/bin/gosu \
&& chown root:user /usr/local/bin/gosu \
&& chmod +s /usr/local/bin/gosu \
# Install python environment
&& pip install -r /tmp/requirements.txt \
# Install gunicorn
&& pip install gunicorn \
&& apt-get purge -y --auto-remove \
		build-essential \
		ca-certificates \
		libmysqlclient-dev \
		python3-dev \
		wget \
&& rm -rf /var/lib/apt/lists/* 

RUN mkdir -p /code && chown user:user /code \
&& mkdir -p /home/user/.ssh && chown user:user /home/user/.ssh

ADD entrypoint.sh /entrypoint.sh

WORKDIR /code
USER user
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python"]
