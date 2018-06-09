FROM centos:centos6  
  
MAINTAINER fabric8.io <fabric8@googlegroups.com>  
  
RUN yum install -y git wget tar gcc bzip2 libxslt-devel libxml2-devel libXt-
devel tmux  
  
RUN rpm -ivh http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-
centos94-9.4-1.noarch.rpm && \  
sed -i 's/^gpgkey.*/&\nexclude=postgresql*/' /etc/yum.repos.d/CentOS-Base.repo
&& \  
yum -y install postgresql94 postgresql94-contrib postgresql94-server
postgresql94-devel postgresql94-libs && \  
service postgresql-9.4 initdb && \  
sed -i "/^host/s/ident/md5/g" /var/lib/pgsql/9.4/data/pg_hba.conf && \  
chkconfig postgresql-9.4 on && \  
service postgresql-9.4 start && \  
echo -e "taiga\ntaiga\n" | su - postgres -c "createuser --pwprompt taiga" && \  
su - postgres -c "createdb taiga -O taiga"  
  
RUN wget --directory-prefix=/tmp
http://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh  
RUN bash /tmp/Miniconda3-3.7.0-Linux-x86_64.sh -b -p /usr/local/miniconda3  
  
RUN adduser taiga  
  
RUN mkdir -p /var/log/taiga && \  
mkdir -p /opt/taiga-front && \  
mkdir -p /opt/taiga-back && \  
mkdir -p /opt/taiga-events  
  
RUN git clone -b stable https://github.com/taigaio/taiga-back.git /opt/taiga-
back  
  
ENV PATH /usr/local/miniconda3/bin:$PATH  
  
  
RUN conda create --yes -n taiga python && \  
source activate root && \  
conda install --yes pip  
  
ENV PATH /usr/local/miniconda3/envs/taiga/bin/:$PATH  
ENV PATH $PATH:/usr/pgsql-9.4/bin/  
  
RUN cd /opt/taiga-back && pip install -r requirements.txt  
  
# clone the front end static content and mount it for a web server to serve up  
RUN git clone -b stable https://github.com/taigaio/taiga-front-dist.git
/opt/taiga-front  
ADD taiga.conf /home/taiga/conf/  
ADD nginx.conf /home/taiga/conf/  
  
VOLUME /opt/taiga-back/static/  
VOLUME /opt/taiga-front/dist  
VOLUME /home/taiga/conf/  
  
ADD start.sh /home/taiga/  
CMD /home/taiga/start.sh  

