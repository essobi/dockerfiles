FROM tomcat:7-jre7  
  
ENV OPENMRS_HOME /root/.OpenMRS  
ENV OPENMRS_MODULES ${OPENMRS_HOME}/modules  
ENV OPENMRS_PLATFORM_VERSION="1.11.7"  
ENV
OPENMRS_PLATFORM_URL="http://sourceforge.net/projects/openmrs/files/releases/OpenMRS_Platform_1.11.7/openmrs.war/download"  
ENV OPENMRS_REFERENCE_VERSION="2.3.1"  
ENV
OPENMRS_REFERENCE_URL="http://sourceforge.net/projects/openmrs/files/releases/OpenMRS_2.3.1/openmrs-2.3.1-modules.zip/download"  
ENV DATABASE_SCRIPT_FILE="openmrs_1.11.7_2.3.1.sql.zip"  
ENV DATABASE_SCRIPT_PATH="db/${DATABASE_SCRIPT_FILE}"  
ENV OPENHMIS_DATABASE_SCRIPT_FILE="openhmis_demo_data_2.x.sql.zip"  
ENV OPENHMIS_DATABASE_SCRIPT_PATH="db/${OPENHMIS_DATABASE_SCRIPT_FILE}"  
ENV
OPENHMIS_LOCAL_DATABASE_SCRIPT_PATH="/root/temp/db/${OPENHMIS_DATABASE_SCRIPT_FILE}"  
ENV DEFAULT_DB_NAME="openmrs_1_11_7_ref_2_3_1"  
ENV DEFAULT_OPENMRS_DB_USER="openmrs_user"  
ENV DEFAULT_OPENMRS_DB_PASS="Openmrs123"  
ENV DEFAULT_OPENMRS_DATABASE_SCRIPT="${DATABASE_SCRIPT_FILE}"  
ENV
DEFAULT_OPENMRS_DATABASE_SCRIPT_PATH="/root/temp/db/${DEFAULT_OPENMRS_DATABASE_SCRIPT}"  
ENV DEBIAN_MAIN_CONTRIB_SOURCE="deb http://ftp.us.debian.org/debian jessie
main contrib"  
ENV DEBIAN_SOURCE_LIST_FILE="/etc/apt/sources.list"  
# Add the main contrib mirror for use when installing fonts package for Jasper
Reports  
RUN echo ${DEBIAN_MAIN_CONTRIB_SOURCE} >> ${DEBIAN_SOURCE_LIST_FILE}  
  
# Refresh repositories and add mysql-client and libxml2-utils (for xmllint)  
# Also add vim and less as well as fonts for use for Jasper Reports  
# Download and Deploy OpenMRS  
# Download and copy reference application modules (if defined)  
# Unzip modules and copy to module/ref folder  
# Create database and setup openmrs db user  
RUN apt-get update && apt-get install -y mysql-client libxml2-utils vim less \  
ttf-mscorefonts-installer \  
&& curl -L ${OPENMRS_PLATFORM_URL} -o ${CATALINA_HOME}/webapps/openmrs.war \  
&& curl -L ${OPENMRS_REFERENCE_URL} -o ref.zip \  
&& mkdir -p /root/temp/modules \  
&& unzip -j ref.zip -d /root/temp/modules/  
  
# Copy OpenHMIS dependencies  
COPY modules/dependencies/2.x/*.omod /root/temp/modules/  
  
# Copy OpenMRS properties file  
COPY openmrs-runtime.properties /root/temp/  
  
# Copy default database script  
COPY ${DATABASE_SCRIPT_PATH} /root/temp/db/  
  
# Copy OpenHMIS database script  
COPY ${OPENHMIS_DATABASE_SCRIPT_PATH} /root/temp/db/  
  
# Expose the openmrs directory as a volume  
VOLUME /root/.OpenMRS/  
  
EXPOSE 8080  
# Setup openmrs, optionally load demo data, and start tomcat  
COPY run.sh /run.sh  
ENTRYPOINT ["/run.sh"]  

