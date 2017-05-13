FROM python

RUN apt-get update && apt-get install -y --no-install-recommends \
   	gcc \
	git \
	libpq-dev \
    && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

VOLUME ["/usr/src/app"]