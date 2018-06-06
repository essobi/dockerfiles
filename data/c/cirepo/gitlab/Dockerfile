  
FROM gitlab/gitlab-ce:10.8.1-ce.0  
VOLUME ["/app/gitlab/data"]  
  
ARG build_fileserver  
ENV ARIA2C_DOWNLOAD aria2c --file-allocation=none -c -x 10 -s 10 -m 0
\--console-log-level=notice --log-level=notice --summary-interval=0  
RUN set -ex \  
&& echo 'tzdata tzdata/Areas select Asia\n\  
tzdata tzdata/Zones/Asia select Shanghai\n\n\  
locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8\n\  
locales locales/default_environment_locale select en_US.UTF-8\n' >
/etc/debconf.txt \  
&& sed -i
's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.163.com\/ubuntu\//g'
/etc/apt/sources.list \  
&& apt-get update -y \  
&& apt-get -yq install --reinstall locales tzdata debconf \  
&& debconf-set-selections /etc/debconf.txt \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& dpkg-reconfigure -f noninteractive locales \  
# && apt-get upgrade -y \  
&& apt-get install -y apt-transport-https aria2 build-essential ca-
certificates curl httpie jq nano net-tools python python-pip unzip vim wget \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
#COPY docker/wait-for-it.sh /app/gitlab/wait-for-it.sh  
RUN echo ===== Install waitforit ===== \  
&& ${ARIA2C_DOWNLOAD} -d /usr/bin -o "waitforit"
"http://o9wbz99tz.bkt.clouddn.com/maxcnunes/waitforit/releases/download/v2.2.0/waitforit-
linux_amd64" \  
&& chmod 755 /usr/bin/waitforit  
  
COPY docker/default_deploy_key.pub /app/gitlab/data/default_deploy_key.pub  
COPY docker/gitlab_utils.sh /app/gitlab/gitlab_utils.sh  
COPY docker/git_init.sh /app/gitlab/git_init.sh  
COPY docker/entrypoint.sh /app/gitlab/entrypoint.sh  
RUN chmod 755 /app/gitlab/*.sh  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
#ENV JAVA_OPTS -Duser.language=zh -Duser.region=CN -Dfile.encoding='UTF-8'
-Duser.timezone='Asia/Shanghai'  
ENTRYPOINT ["/app/gitlab/entrypoint.sh"]  
CMD ["/assets/wrapper"]  

