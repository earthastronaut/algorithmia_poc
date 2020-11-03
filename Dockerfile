# ########################### #
# Base Image
# ########################### #

FROM python:3.7-buster as base

ENV ENVIRONMENT=""

WORKDIR /usr/local/src/app

COPY requirements.txt .
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

COPY bin ./bin
COPY src ./src
COPY app_config.yml .

ENV PYTHONPATH=${PWD} 
ENV PATH=${PWD}/bin:${PATH}

CMD ["run.py"]

# ########################### #
# Dev Work Image
# ########################### #

FROM base as dev 

ENV ENVIRONMENT="DEV"

WORKDIR /work

COPY requirements_dev.txt .
RUN pip install --no-cache-dir -r requirements_dev.txt

ENV PYTHONPATH=${PWD} 
ENV PATH=${PWD}/bin:${PATH}

EXPOSE 8888

CMD [ "jupyter", "lab" ]

# ########################### #
# Production Image
# ########################### #

FROM base as production

EXPOSE 5000

ENV ENVIRONMENT="PRODUCTION"
