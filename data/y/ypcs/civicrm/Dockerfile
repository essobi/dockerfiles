FROM ypcs/drupal:latest  
  
ENV CIVICRM_ENVIRONMENT production  
  
ENV CIVICRM_DATABASE_DSN mysql://civicrm:civicrm@db/civicrm  
ENV CIVICRM_URL http://civicrm/  
  
ENV CIVICRM_VERSION 5.0.0  
ENV CIVICRM_SHA256
cd2a3ca74a1740f8cb9267da487028522adebde58ed7f994c2ac0c772ae56796  
ENV CIVICRM_L10N_SHA256
ce7add5db3b0098af93de1742f0dad88157cd66e2b8eae9133c327403d080e35  
  
ENV CIVICRM_CV_SHA256
500bcc61900baf59a98eef5c1bdedc4c1559fbd9339413573213ca84a5a3fef5  
ENV CIVICRM_CV_URL https://download.civicrm.org/cv/cv.phar  
  
ARG VCS_REF  
LABEL org.label-schema.vcs-ref=$VCS_REF  
  
RUN \  
/usr/local/sbin/docker-upgrade &&\  
apt-get update && \  
apt-get --assume-yes upgrade && \  
apt-get --assume-yes install \  
curl \  
mariadb-client && \  
/usr/local/sbin/docker-cleanup  
  
RUN \  
curl -fSL "${CIVICRM_CV_URL}" -o /usr/local/bin/cv && \  
echo "${CIVICRM_CV_SHA256} /usr/local/bin/cv" |sha256sum -c - && \  
chmod +x /usr/local/bin/cv  
  
COPY download.sh /usr/local/sbin/civicrm-download  
COPY install.sh /usr/local/sbin/civicrm-install  
  
COPY config/*.php /usr/local/share/civicrm/  
  
RUN echo "Source: https://github.com/ypcs/docker-civicrm\nBuild date: $(date
--iso-8601=ns)" >/README  

