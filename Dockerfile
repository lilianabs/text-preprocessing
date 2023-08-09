ARG BASE_IMAGE=python:3.9

FROM ${BASE_IMAGE} as base

WORKDIR /opt

ENV PYTHONUNBUFFERED TRUE

COPY requirements.txt .
COPY requirements_dev.txt .

# Install python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir wheel \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -r requirements_dev.txt \
    && pip list