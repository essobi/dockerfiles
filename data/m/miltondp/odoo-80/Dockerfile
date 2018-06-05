FROM miltondp/odoo-base:latest  
  
USER root  
  
# Update Odoo configuration file  
COPY ./openerp-server.conf /etc/odoo/  
  
  
# Locales  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y && apt-get install -y --no-install-recommends locales \  
&& echo 'es_AR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen \  
&& echo 'es_US.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen \  
&& echo 'C.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen \  
&& dpkg-reconfigure locales && /usr/sbin/update-locale LANG=C.UTF-8 \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /root/.ssh  
  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
# Debian packages  
RUN apt-get update -y && apt-get install -y \  
python-pip python-gevent python-dev python-matplotlib font-manager \  
swig libffi-dev libssl-dev python-m2crypto python-httplib2 libcups2-dev \  
&& rm -rf /var/lib/apt/lists/*  
# Python packages  
RUN apt-get update -y && apt-get install -y --no-install-recommends git \  
&& pip install psycogreen==1.0 mercadopago==0.3.4 geopy==0.95.1
BeautifulSoup==3.2.1 suds==0.4 \  
git+https://github.com/aeroo/aeroolib.git@master pycups==1.9.68 \  
genshi==0.6.1 pyOpenSSL==0.15.1 openerp-client-lib==1.1.2 fabric==1.10.2
erppeek==1.6.1 fabtools==0.19.0 \  
xlrd==0.9.4 unicodecsv==0.13.0 python-magic==0.4.6 \  
&& apt-get purge -y --auto-remove git \  
&& rm -rf /var/lib/apt/lists/*  
  
# pyafipws  
RUN apt-get update -y && apt-get install -y --no-install-recommends wget \  
&& cd /tmp \  
&& wget https://github.com/reingart/pyafipws/archive/2.7.1872.tar.gz \  
&& tar -xf 2.7.1872.tar.gz \  
&& cd pyafipws-2.7.1872 \  
&& pip install -r requirements.txt \  
&& python setup.py install \  
&& cd .. \  
&& rm -rf 2.7.1872.tar.gz pyafipws-2.7.1872 \  
&& chmod 777 -R /usr/local/lib/python2.7/dist-
packages/PyAfipWs-2.7.0-py2.7.egg/ \  
&& apt-get purge -y --auto-remove wget \  
&& rm -rf /var/lib/apt/lists/*  
# ingadhoc addons  
ENV INGADHOC_BRANCH 8.0  
COPY id_bot /root/.ssh/id_rsa  
RUN apt-get update -y && apt-get install -y --no-install-recommends git
openssh-client \  
&& mkdir -p /mnt/addons/ingadhoc && cd /mnt/addons/ingadhoc \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/account-
analytic.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/account-
financial-tools.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/account-
invoicing.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/account-
payment.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/crm.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/hr.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/manufacture.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/miscellaneous.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/multi-
company.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/partner.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/product.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/project.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/purchase.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/reporting-engine.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/sale.git
\  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/stock.git
\  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/survey.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/surveyor.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/website.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/odoo-
etl.git \  
&& mkdir /mnt/addons/others && cd /mnt/addons/others \  
&& git clone https://bitbucket.org/BizzAppDev/oerp_no_phoning_home.git
stop_phoning \  
&& touch /root/.ssh/known_hosts && ssh-keyscan -T 120 bitbucket.org >>
/root/.ssh/known_hosts \  
&& cd /mnt/addons \  
&& chmod 400 /root/.ssh/id_rsa \  
&& git clone git@bitbucket.org:miltondp/odoo-folder-addons.git folder \  
&& rm -rf /root/.ssh \  
&& cd /mnt/addons \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/ingadhoc/odoo-
argentina.git \  
&& git clone --branch ${INGADHOC_BRANCH}
https://github.com/ingadhoc/aeroo_reports.git \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/OCA/server-tools
oca-server-tools \  
&& git clone --branch ${INGADHOC_BRANCH} https://github.com/OCA/web oca-web \  
&& chown -R odoo.odoo /mnt/addons \  
&& apt-get purge -y --auto-remove git openssh-client \  
&& rm -rf /var/lib/apt/lists/*  
# Disable auto_install for some modules  
RUN sed -i "s/'auto_install': True/'auto_install': False/"
/usr/lib/python2.7/dist-packages/openerp/addons/im_odoo_support/__openerp__.py
\  
&& sed -i "s/'auto_install': True/'auto_install': False/"
/usr/lib/python2.7/dist-packages/openerp/addons/portal/__openerp__.py  
# sed -i "s/'auto_install': True/'auto_install': False/"
/usr/lib/python2.7/dist-packages/openerp/addons/bus/__openerp__.py \  
# sed -i "s/'auto_install': True/'auto_install': False/"
/usr/lib/python2.7/dist-packages/openerp/addons/base_import/__openerp__.py \  
# sed -i "s/'auto_install': True/'auto_install': False/"
/usr/lib/python2.7/dist-packages/openerp/addons/im_chat/__openerp__.py  
  
  
USER odoo  
  

