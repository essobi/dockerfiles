FROM java:8-jdk  
  
MAINTAINER Dino.Korah@redmatter.com  
  
ENV TZ="Europe/London" \  
MAMUTE_VERSION="1.4.0" \  
MAMUTE_INSTALL_DIR="/mamute" \  
VRAPTOR_ENV="production"  
  
ADD entrypoint.sh hibernate.cfg.xml production.properties /tmp/  
  
RUN ( \  
export DEBIAN_FRONTEND=noninteractive; \  
  
BUILD_DEPS="fastjar"; \  
APP_DEPS=""; \  
  
WAR_URL="https://github.com/caelum/mamute/releases/download/v${MAMUTE_VERSION}/mamute-${MAMUTE_VERSION}.war";
\  
  
set -e -u -x; \  
if [ -n "${BUILD_DEPS}${APP_DEPS}" ]; then \  
apt-get update; \  
apt-get -y upgrade; \  
apt-get install -y --no-install-recommends ${APP_DEPS} ${BUILD_DEPS}; \  
fi; \  
  
wget -q ${WAR_URL} -O /tmp/mamute.war; \  
  
mkdir -p ${MAMUTE_INSTALL_DIR}; \  
cd ${MAMUTE_INSTALL_DIR}; \  
  
jar xvf /tmp/mamute.war; \  
rm /tmp/mamute.war; \  
  
sed -ie 's/java/exec java/g' run.sh; \  
chmod +x run.sh; \  
  
mv /tmp/production.properties WEB-INF/classes/production.properties; \  
mv /tmp/hibernate.cfg.xml WEB-INF/classes/production/hibernate.cfg.xml; \  
mv /tmp/entrypoint.sh /entrypoint.sh && chmod +x /entrypoint.sh; \  
if [ -n "${BUILD_DEPS}${APP_DEPS}" ]; then \  
[ -n "$BUILD_DEPS" ] && apt-get remove -y $BUILD_DEPS; \  
apt-get clean autoclean; \  
apt-get autoremove --yes; \  
fi; \  
rm -rf /var/lib/{apt,dpkg,cache,log}/; \  
)  
  
EXPOSE 80  
  
ENTRYPOINT ["/entrypoint.sh", "run"]  
  

