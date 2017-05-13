FROM mcpayment/ubuntu1604

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        python-pip \
        python-virtualenv \
        python-yaml \
        python-dev \
        gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 
