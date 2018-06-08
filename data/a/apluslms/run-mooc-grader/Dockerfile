FROM apluslms/run-python3  
  
# Required paths  
RUN mkdir -p /srv/courses/default /srv/data /srv/grader /srv/grader_static/ \  
&& chmod 1777 /srv/data /srv/grader_static/  
COPY up.sh docker-compose-run.sh /srv/  
  
# Install system packages  
RUN apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy
--no-install-recommends \  
-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \  
apt-transport-https \  
software-properties-common \  
curl \  
gnupg2 \  
libxml2-dev \  
libxslt-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# Install docker-ce  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
>/dev/null 2>&1 \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian stretch stable" \  
&& apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy
--no-install-recommends \  
-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \  
docker-ce \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# Set container related configuration via environment variables  
WORKDIR /srv/grader/  
ENV HOME=/srv/data \  
GRADER_DB_FILE=/srv/data/mgrader.sqlite3 \  
GRADER_SECRET_KEY_FILE=/srv/data/mgrader_secret_key.py \  
GRADER_AJAX_KEY_FILE=/srv/data/mgrader_ajax_key.py  
ENV DJANGO_DEBUG=true \  
GRADER_CONTAINER_MODE=true \  
DJANGO_CONTAINER_SCRIPT=/srv/docker-compose-run.sh \  
GRADER_PERSONALIZED_CONTENT_PATH=/srv/data/mgrader_ex-meta \  
GRADER_SUBMISSION_PATH=/srv/data/mgrader_uploads \  
GRADER_STATIC_ROOT=/srv/grader_static/ \  
DJANGO_CACHES="{\"default\": {\"BACKEND\":
\"django.core.cache.backends.dummy.DummyCache\"}}" \  
GRADER_DATABASES="{\"default\": {\"ENGINE\": \"django.db.backends.sqlite3\",
\"NAME\": \"$GRADER_DB_FILE\"}}" \  
GRADER_STATIC_URL_HOST_INJECT="http://localhost:8080"  
  
# Install the application and requirements  
# 1) clone, touch local_settings to suppress warnings, prebuild .pyc files  
# 2) install requirements, remove the file, remove unrequired locales and
tests  
# 3) create database  
RUN git clone https://github.com/Aalto-LeTech/mooc-grader.git . \  
&& (echo "On branch $(git rev-parse --abbrev-ref HEAD) | $(git describe)";
echo; git log -n5) > GIT \  
&& rm -rf .git \  
&& python3 -m compileall -q . \  
\  
&& pip3 --no-cache-dir --disable-pip-version-check install -r requirements.txt
\  
&& rm requirements.txt \  
&& find /usr/local/lib/python* -type d -regex '.*/locale/[a-z_A-Z]+' -not
-regex '.*/\\(en\|fi\|sv\\)' -print0 | xargs -0 rm -rf \  
&& find /usr/local/lib/python* -type d -name 'tests' -print0 | xargs -0 rm -rf
\  
\  
&& mkdir -p /srv/grader/courses/ \  
&& ln -s -T /srv/courses/default /srv/grader/courses/default \  
\  
&& python3 manage.py migrate \  
&& touch $GRADER_DB_FILE && chmod 0777 $GRADER_DB_FILE \  
&& rm -rf $GRADER_SUBMISSION_PATH \  
&& rm -rf $GRADER_SECRET_KEY_FILE $GRADER_AJAX_KEY_FILE  
  
VOLUME /srv/data  
VOLUME /srv/courses/default  
VOLUME /srv/grader_static/  
EXPOSE 8080  
ENTRYPOINT [ "/srv/up.sh" ]  

