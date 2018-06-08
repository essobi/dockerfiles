FROM apluslms/grading-base:2.2  
  
RUN apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy
--no-install-recommends \  
-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \  
python3 \  
python3-pip \  
python3-setuptools \  
&& ln -s /usr/bin/python3 /usr/local/bin/python \  
&& ln -s /usr/bin/pip3 /usr/local/bin/pip \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN pip3 --no-cache-dir --disable-pip-version-check install \  
https://github.com/Aalto-LeTech/python-grader-utils/archive/master.tar.gz \  
&& find /usr/local/lib/python* -type d -regex '.*/locale/[a-z_A-Z]+' -not
-regex '.*/\\(en\|fi\|sv\\)' -print0 | xargs -0 rm -rf \  
&& find /usr/local/lib/python* -type d -name 'tests' -print0 | xargs -0 rm -rf  
  
COPY bin /usr/local/bin  
RUN chmod 0555 /usr/local/bin/*  

