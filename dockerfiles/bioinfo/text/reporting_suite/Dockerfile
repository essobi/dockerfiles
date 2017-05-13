FROM stackbrew/ubuntu:14.04
MAINTAINER Justin Johnson "https://github.com/bioinfo

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/AstraZeneca-NGS/Reporting_Suite.git /usr/local/src && \
    ln -s /usr/local/src/Reporting_Suite /usr/local/src/az.reporting
