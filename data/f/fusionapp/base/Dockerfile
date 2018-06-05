FROM pypy:2-6.0.0-slim  
# See https://github.com/debuerreotype/debuerreotype/issues/10  
RUN mkdir -p /usr/share/man/man1  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-
install-recommends -qy dpkg-dev gcc libc6-dev libffi-dev libssl-dev
libxml2-dev libxslt1-dev libsqlite3-dev ca-certificates libjpeg-dev zlib1g-dev
git jarwrapper openjdk-7-jre-headless curl locales pdftk  
RUN echo 'en_ZA.UTF-8 UTF-8\nen_US.UTF-8 UTF-8\nen_GB.UTF-8 UTF-8' >
/etc/locale.gen && locale-gen  
RUN pip install --no-cache-dir virtualenv && pypy -m virtualenv /appenv  
COPY ["requirements.txt", "/appenv/requirements.txt"]  
RUN . /appenv/bin/activate && pip install --no-cache-dir --requirement
/appenv/requirements.txt  
WORKDIR /application  
CMD [ \  
"/appenv/bin/pip", "wheel", \  
"--wheel-dir", "/wheelhouse", \  
"--find-links", "/wheelhouse", \  
"--no-cache-dir", \  
"--requirement", "/application/requirements.txt", "/application"]  

